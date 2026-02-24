"""
load_data.py
------------
Loads cleaned DataFrames into PostgreSQL.
Uses upsert logic (INSERT ... ON CONFLICT DO NOTHING) so the pipeline
is safely re-runnable without creating duplicates.
"""

import logging
import pandas as pd
from db_config import get_connection

logger = logging.getLogger(__name__)


def load_courses(df: pd.DataFrame) -> int:
    """Upsert courses into DB. Returns number of rows inserted."""
    query = """
        INSERT INTO courses (course_code, course_name, credits, program_code, course_type)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (course_code) DO NOTHING;
    """
    conn = get_connection()
    inserted = 0
    try:
        with conn.cursor() as cur:
            for _, row in df.iterrows():
                cur.execute(query, (
                    row["course_code"],
                    row["course_name"],
                    int(row["credits"]),
                    row["program_code"],
                    row["course_type"],
                ))
                inserted += cur.rowcount
        conn.commit()
        logger.info("Loaded %d new course rows into DB.", inserted)
    except Exception as e:
        conn.rollback()
        logger.error("Error loading courses: %s", e)
        raise
    finally:
        conn.close()
    return inserted


def load_prerequisites(df: pd.DataFrame) -> int:
    """Upsert prerequisites into DB. Returns number of rows inserted."""
    query = """
        INSERT INTO prerequisites (course_code, required_course_code)
        VALUES (%s, %s)
        ON CONFLICT (course_code, required_course_code) DO NOTHING;
    """
    conn = get_connection()
    inserted = 0
    try:
        with conn.cursor() as cur:
            for _, row in df.iterrows():
                cur.execute(query, (row["course_code"], row["required_course_code"]))
                inserted += cur.rowcount
        conn.commit()
        logger.info("Loaded %d new prerequisite rows into DB.", inserted)
    except Exception as e:
        conn.rollback()
        logger.error("Error loading prerequisites: %s", e)
        raise
    finally:
        conn.close()
    return inserted


def load_data(cleaned: dict) -> dict:
    """
    Master load function — called by Airflow task.
    Loads all cleaned DataFrames into their respective tables.
    Returns counts of inserted rows.
    """
    return {
        "courses_inserted":       load_courses(cleaned["courses"]),
        "prerequisites_inserted": load_prerequisites(cleaned["prerequisites"]),
    }


if __name__ == "__main__":
    import logging
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from acquire_data import acquire_data
    from preprocess_data import preprocess_data
    from validate_data import validate_data

    logging.basicConfig(level=logging.INFO)
    raw     = acquire_data()
    cleaned = preprocess_data(raw)
    validate_data(cleaned)
    counts  = load_data(cleaned)
    print("\nLoad complete:", counts)