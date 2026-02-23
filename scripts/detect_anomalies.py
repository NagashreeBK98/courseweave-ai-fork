"""
detect_anomalies.py
-------------------
Detects data anomalies AFTER the data is loaded into PostgreSQL.
Runs SQL-based checks directly against the live DB.

Anomalies checked:
- Circular prerequisite chains
- Students who completed a course without meeting prerequisites

Logs warnings for soft anomalies.
Logs errors for hard anomalies (data integrity issues).
"""

import logging
from db_config import get_connection

logger = logging.getLogger(__name__)


def detect_missing_prerequisites() -> list[dict]:
    """
    Find students who completed a course but haven't completed its prerequisite.
    This is a data integrity issue worth flagging.
    """
    query = """
        SELECT s.email, sc.course_code AS enrolled_course,
               p.required_course_code AS missing_prereq
        FROM student_courses sc
        JOIN students s ON sc.student_id = s.id
        JOIN prerequisites p ON sc.course_code = p.course_code
        WHERE NOT EXISTS (
            SELECT 1 FROM student_courses sc2
            WHERE sc2.student_id = sc.student_id
              AND sc2.course_code = p.required_course_code
        );
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = [dict(r) for r in cur.fetchall()]
        if rows:
            logger.error(
                "ANOMALY [missing_prerequisites]: %d students completed courses "
                "without satisfying prerequisites.", len(rows)
            )
        else:
            logger.info("No missing prerequisite anomalies found.")
        return rows
    finally:
        conn.close()


def detect_circular_prerequisites() -> list[dict]:
    """
    Detect circular prerequisite chains using a recursive CTE.
    E.g. A -> B -> A is invalid.
    """
    query = """
        WITH RECURSIVE prereq_chain AS (
            SELECT course_code, required_course_code,
                   ARRAY[course_code]::varchar[] AS visited,
                   FALSE AS is_cycle
            FROM prerequisites

            UNION ALL

            SELECT p.course_code, p.required_course_code,
                   visited || p.course_code,
                   p.course_code = ANY(visited)
            FROM prerequisites p
            JOIN prereq_chain pc ON p.course_code = pc.required_course_code
            WHERE NOT pc.is_cycle
        )
        SELECT DISTINCT course_code, required_course_code
        FROM prereq_chain
        WHERE is_cycle = TRUE;
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = [dict(r) for r in cur.fetchall()]
        if rows:
            logger.error(
                "ANOMALY [circular_prerequisites]: Circular dependency detected: %s", rows
            )
        else:
            logger.info("No circular prerequisite anomalies found.")
        return rows
    finally:
        conn.close()


def detect_anomalies() -> dict:
    """
    Master anomaly detection function -- called by Airflow task.
    Returns a summary dict of all detected anomalies.
    """
    logger.info("Running anomaly detection...")

    results = {
        "missing_prerequisites":  detect_missing_prerequisites(),
        "circular_prerequisites": detect_circular_prerequisites(),
    }

    hard_anomalies = (
        len(results["missing_prerequisites"]) +
        len(results["circular_prerequisites"])
    )

    if hard_anomalies > 0:
        logger.error(
            "Anomaly detection complete -- %d HARD anomalies found. "
            "Review logs immediately.", hard_anomalies
        )
    else:
        logger.info("Anomaly detection complete -- no hard anomalies found.")

    return results


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    results = detect_anomalies()
    for check, rows in results.items():
        print(f"\n[{check}] -> {len(rows)} anomalies")