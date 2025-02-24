import pytest
import pandas as pd

def test_row_count():
    """
    Test the row count of the dataset.
    """
    data = pd.read_csv("data/census.csv")
    assert 32000 < data.shape[0] < 33000

def test_columns():
    """
    This test verifies that all expected columns exist in the dataset.
    """
    expected_columns = [
        "age", "workclass", "fnlgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ]

    data = pd.read_csv("data/census.csv")
    missing_columns = [col for col in expected_columns if col not in data.columns]
    assert not missing_columns, f"Missing columns: {missing_columns}"

    print("✅ test_columns passed!")

def test_salary_variable():
    """
    This test ensures that the 'salary' column contains only the expected labels.
    """
    data = pd.read_csv("data/census.csv")
    target_values = data["salary"].unique()
    expected_values = {">50K", "<=50K"}
    
    assert set(target_values).issubset(expected_values), f"Unexpected salary labels found: {set(target_values)}"
    print("✅ test_salary_variable passed!")