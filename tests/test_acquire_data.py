"""
test_acquire_data.py
Tests for the data acquisition layer.
"""

import pandas as pd
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from acquire_data import acquire_courses, acquire_prerequisites, acquire_data


def test_acquire_courses_returns_dataframe():
    df = acquire_courses()
    assert isinstance(df, pd.DataFrame)


def test_acquire_courses_has_required_columns():
    df = acquire_courses()
    expected = {"course_code", "course_name", "credits", "program_code", "course_type"}
    assert expected.issubset(set(df.columns))


def test_acquire_courses_not_empty():
    df = acquire_courses()
    assert len(df) > 0


def test_acquire_prerequisites_returns_dataframe():
    df = acquire_prerequisites()
    assert isinstance(df, pd.DataFrame)


def test_acquire_prerequisites_has_required_columns():
    df = acquire_prerequisites()
    assert {"course_code", "required_course_code"}.issubset(set(df.columns))


def test_acquire_data_returns_dict_with_both_tables():
    data = acquire_data()
    assert "courses" in data
    assert "prerequisites" in data
    assert isinstance(data["courses"], pd.DataFrame)
    assert isinstance(data["prerequisites"], pd.DataFrame)