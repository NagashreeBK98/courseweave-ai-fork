"""
test_validate_data.py
Tests for the schema validation layer.
"""

import pandas as pd
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from validate_data import validate_courses, validate_prerequisites, generate_statistics


@pytest.fixture
def clean_courses():
    return pd.DataFrame({
        "course_code":  ["IE6400", "IE6700", "CS5800"],
        "course_name":  ["Foundations", "Data Mgmt", "Algorithms"],
        "credits":      [4, 4, 4],
        "program_code": ["MS_DAE", "MS_DAE", "MS_CS"],
        "course_type":  ["Core", "Core", "Core"],
    })


@pytest.fixture
def clean_prereqs():
    return pd.DataFrame({
        "course_code":          ["IE7275"],
        "required_course_code": ["IE6400"],
    })


def test_valid_courses_no_violations(clean_courses):
    violations = validate_courses(clean_courses)
    assert violations == []


def test_null_course_code_flagged():
    df = pd.DataFrame({
        "course_code":  [None],
        "course_name":  ["Test"],
        "credits":      [4],
        "program_code": ["MS_DAE"],
        "course_type":  ["Core"],
    })
    violations = validate_courses(df)
    assert any(v["check"] == "no_nulls" for v in violations)


def test_duplicate_course_code_flagged():
    df = pd.DataFrame({
        "course_code":  ["IE6400", "IE6400"],
        "course_name":  ["A", "B"],
        "credits":      [4, 4],
        "program_code": ["MS_DAE", "MS_DAE"],
        "course_type":  ["Core", "Core"],
    })
    violations = validate_courses(df)
    assert any(v["check"] == "unique_course_code" for v in violations)


def test_invalid_program_code_flagged():
    df = pd.DataFrame({
        "course_code":  ["IE6400"],
        "course_name":  ["Foundations"],
        "credits":      [4],
        "program_code": ["MS_FAKE"],
        "course_type":  ["Core"],
    })
    violations = validate_courses(df)
    assert any(v["check"] == "valid_program_code" for v in violations)


def test_valid_prerequisites_no_violations(clean_prereqs):
    valid_codes = {"IE6400", "IE7275"}
    violations = validate_prerequisites(clean_prereqs, valid_codes)
    assert violations == []


def test_self_referencing_prereq_flagged():
    df = pd.DataFrame({
        "course_code":          ["IE6400"],
        "required_course_code": ["IE6400"],
    })
    violations = validate_prerequisites(df, {"IE6400"})
    assert any(v["check"] == "no_self_reference" for v in violations)


def test_generate_statistics_keys(clean_courses, clean_prereqs):
    stats = generate_statistics({"courses": clean_courses, "prerequisites": clean_prereqs})
    assert "courses" in stats
    assert "prerequisites" in stats
    assert "total_courses" in stats["courses"]
    assert "total_prereq_pairs" in stats["prerequisites"]