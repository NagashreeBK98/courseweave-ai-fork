"""
acquire_data.py
---------------
Loads raw CSV files into pandas DataFrames.

This is the ONLY function that knows where data comes from.
Swap this file later to pull from a UI form, API, or web scraper —
nothing downstream needs to change.
"""

import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"


def acquire_courses() -> pd.DataFrame:
    """Read raw courses CSV → DataFrame."""
    path = RAW_DIR / "courses.csv"
    logger.info("Acquiring courses from %s", path)
    df = pd.read_csv(path)
    logger.info("Acquired %d course records.", len(df))
    return df


def acquire_prerequisites() -> pd.DataFrame:
    """Read raw prerequisites CSV → DataFrame."""
    path = RAW_DIR / "prerequisites.csv"
    logger.info("Acquiring prerequisites from %s", path)
    df = pd.read_csv(path)
    logger.info("Acquired %d prerequisite records.", len(df))
    return df


def acquire_data() -> dict[str, pd.DataFrame]:
    """
    Master acquisition function — called by Airflow task.
    Returns a dict of DataFrames keyed by table name.
    """
    return {
        "courses":       acquire_courses(),
        "prerequisites": acquire_prerequisites(),
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = acquire_data()
    for name, df in data.items():
        print(f"\n--- {name} ({len(df)} rows) ---")
        print(df.head())