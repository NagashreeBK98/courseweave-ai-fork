"""
preprocess_data.py
------------------
Cleans and transforms raw DataFrames before DB load.
Each function is modular and independently testable.
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)

VALID_PROGRAM_CODES = {"MS_DAE", "MS_DS", "MS_CS", "MS_DA", "MS_IS"}
VALID_COURSE_TYPES  = {"Core", "Elective"}
VALID_CREDITS       = {4}


def preprocess_courses(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate courses DataFrame.

    Transformations applied:
    - Drop nulls in required fields FIRST (before type casting)
    - Strip whitespace from string columns
    - Uppercase course_code and program_code
    - Title-case course_type
    - Drop duplicates on course_code
    - Filter to valid program_codes and course_types
    - Validate credits are within expected range
    """
    logger.info("Preprocessing courses — input shape: %s", df.shape)
    original_len = len(df)

    # Drop nulls FIRST before any type casting
    required = ["course_code", "course_name", "credits", "program_code", "course_type"]
    before = len(df)
    df = df.dropna(subset=required).copy()
    dropped_nulls = before - len(df)
    if dropped_nulls:
        logger.warning("Dropped %d rows with null required fields.", dropped_nulls)

    # Now safe to strip and normalise
    str_cols = ["course_code", "course_name", "program_code", "course_type"]
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    df["course_code"]  = df["course_code"].str.upper()
    df["program_code"] = df["program_code"].str.upper()
    df["course_type"]  = df["course_type"].str.title()

    # Drop duplicates
    before = len(df)
    df = df.drop_duplicates(subset=["course_code"])
    dropped_dupes = before - len(df)
    if dropped_dupes:
        logger.warning("Dropped %d duplicate course_code rows.", dropped_dupes)

    # Validate program_code
    invalid_programs = ~df["program_code"].isin(VALID_PROGRAM_CODES)
    if invalid_programs.any():
        bad = df.loc[invalid_programs, "program_code"].unique().tolist()
        logger.warning("Unknown program_codes found and removed: %s", bad)
        df = df[~invalid_programs]

    # Validate course_type
    invalid_types = ~df["course_type"].isin(VALID_COURSE_TYPES)
    if invalid_types.any():
        bad = df.loc[invalid_types, "course_type"].unique().tolist()
        logger.warning("Unknown course_types found and removed: %s", bad)
        df = df[~invalid_types]

    # Validate credits
    invalid_credits = ~df["credits"].isin(VALID_CREDITS)
    if invalid_credits.any():
        bad = df.loc[invalid_credits, ["course_code", "credits"]].to_dict("records")
        logger.warning("Unexpected credit values: %s", bad)

    df = df.reset_index(drop=True)
    logger.info(
        "Preprocessing complete — output shape: %s (removed %d rows total).",
        df.shape, original_len - len(df)
    )
    return df


def preprocess_prerequisites(
    df: pd.DataFrame, valid_course_codes: set
) -> pd.DataFrame:
    """
    Clean and validate prerequisites DataFrame.

    - Strip and uppercase course codes
    - Drop nulls
    - Drop duplicates
    - Remove rows where either course code doesn't exist in courses table
    """
    logger.info("Preprocessing prerequisites — input shape: %s", df.shape)

    df = df.dropna(subset=["course_code", "required_course_code"])

    df["course_code"]          = df["course_code"].astype(str).str.strip().str.upper()
    df["required_course_code"] = df["required_course_code"].astype(str).str.strip().str.upper()

    df = df.drop_duplicates(subset=["course_code", "required_course_code"])

    # Remove orphaned references
    orphaned = ~(
        df["course_code"].isin(valid_course_codes) &
        df["required_course_code"].isin(valid_course_codes)
    )
    if orphaned.any():
        bad = df[orphaned].to_dict("records")
        logger.warning("Removing prerequisites with unknown course codes: %s", bad)
        df = df[~orphaned]

    df = df.reset_index(drop=True)
    logger.info("Prerequisites preprocessing complete — output shape: %s", df.shape)
    return df


def preprocess_data(raw: dict) -> dict:
    """
    Master preprocessing function — called by Airflow task.
    Accepts the dict returned by acquire_data(), returns cleaned dict.
    """
    courses_clean = preprocess_courses(raw["courses"])
    valid_codes   = set(courses_clean["course_code"])
    prereqs_clean = preprocess_prerequisites(raw["prerequisites"], valid_codes)

    return {
        "courses":       courses_clean,
        "prerequisites": prereqs_clean,
    }


if __name__ == "__main__":
    import logging
    from acquire_data import acquire_data

    logging.basicConfig(level=logging.INFO)
    raw     = acquire_data()
    cleaned = preprocess_data(raw)

    for name, df in cleaned.items():
        print(f"\n--- {name} (cleaned, {len(df)} rows) ---")
        print(df.head())