"""
test_preprocess_data.py
Tests for the preprocessing layer — focuses on edge cases and transformations.
"""

import pandas as pd
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from preprocess_data import preprocess_courses, preprocess_prerequisites


# ─── Fixtures ───────────────────────────────────────────────────────────────

@pytest.fixture
def valid_courses_df():
    return pd.DataFrame({
        "course_code":  ["IE6400", "IE6700", "CS5800"],
        "course_name":  ["Foundations", "Data Mgmt", "Algorithms"],
        "credits":      [4, 4, 4],
        "program_code": ["MS_DAE", "MS_DAE", "MS_CS"],
        "course_type":  ["Core", "Core", "Core"],
    })


@pytest.fixture
def valid_prereqs_df():
    return pd.DataFrame({
        "course_code":          ["IE7275"],
        "required_course_code": ["IE6400"],
    })


# ─── Course preprocessing tests ─────────────────────────────────────────────

def test_preprocess_strips_whitespace(valid_courses_df):
    valid_courses_df.loc[0, "course_code"] = "  IE6400  "
    result = preprocess_courses(valid_courses_df)
    assert result["course_code"].iloc[0] == "IE6400"


def test_preprocess_uppercases_course_code(valid_courses_df):
    valid_courses_df.loc[0, "course_code"] = "ie6400"
    result = preprocess_courses(valid_courses_df)
    assert result["course_code"].iloc[0] == "IE6400"


def test_preprocess_drops_null_course_name(valid_courses_df):
    valid_courses_df.loc[0, "course_name"] = None
    result = preprocess_courses(valid_courses_df)
    assert len(result) == 2


def test_preprocess_drops_duplicate_course_codes(valid_courses_df):
    dupe_row = valid_courses_df.iloc[0].copy()
    df_with_dupe = pd.concat([valid_courses_df, dupe_row.to_frame().T], ignore_index=True)
    result = preprocess_courses(df_with_dupe)
    assert len(result) == 3  # duplicate removed


def test_preprocess_removes_invalid_program_code(valid_courses_df):
    valid_courses_df.loc[0, "program_code"] = "MS_FAKE"
    result = preprocess_courses(valid_courses_df)
    assert "IE6400" not in result["course_code"].values


def test_preprocess_removes_invalid_course_type(valid_courses_df):
    valid_courses_df.loc[0, "course_type"] = "Mandatory"
    result = preprocess_courses(valid_courses_df)
    assert len(result) == 2


def test_preprocess_returns_dataframe(valid_courses_df):
    result = preprocess_courses(valid_courses_df)
    assert isinstance(result, pd.DataFrame)


# ─── Prerequisite preprocessing tests ───────────────────────────────────────

def test_preprocess_prereqs_removes_orphaned_codes():
    valid_codes = {"IE6400", "IE7275"}
    df = pd.DataFrame({
        "course_code":          ["IE7275", "CS9999"],  # CS9999 doesn't exist
        "required_course_code": ["IE6400", "CS8888"],
    })
    result = preprocess_prerequisites(df, valid_codes)
    assert len(result) == 1
    assert result["course_code"].iloc[0] == "IE7275"


def test_preprocess_prereqs_drops_duplicates():
    valid_codes = {"IE6400", "IE7275"}
    df = pd.DataFrame({
        "course_code":          ["IE7275", "IE7275"],
        "required_course_code": ["IE6400", "IE6400"],
    })
    result = preprocess_prerequisites(df, valid_codes)
    assert len(result) == 1


def test_preprocess_prereqs_strips_whitespace():
    valid_codes = {"IE6400", "IE7275"}
    df = pd.DataFrame({
        "course_code":          ["  IE7275  "],
        "required_course_code": ["  IE6400  "],
    })
    result = preprocess_prerequisites(df, valid_codes)
    assert result["course_code"].iloc[0] == "IE7275"