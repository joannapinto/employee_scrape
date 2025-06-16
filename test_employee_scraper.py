import pytest
import pandas as pd
from employee_scraper import normalize_employee_data

# Sample dataset for testing
SAMPLE_DATA = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "12345",
        "gender": "Male",
        "age": 30,
        "salary": 50000,
        "department": "Engineering",
        "hire_date": "2023-01-15",
        "email": "john.doe@example.com",
        "designation": "Data Engineer"
    }
]

def test_normalized_data_structure():
    """
    Test to verify if the normalized DataFrame has all the required columns.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    expected_columns = ['first_name', 'last_name', 'phone', 'email', 'gender', 
                        'age', 'salary', 'department', 'hire_date', 
                        'designation', 'Full Name']
    assert all(col in df.columns for col in expected_columns), "Missing columns in normalized DataFrame"

def test_phone_normalization():
    """
    Test to ensure phone numbers are normalized correctly.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    assert df['phone'].iloc[0] == "12345", "Phone number normalization failed"

def test_missing_email_handling():
    """
    Test to check handling of missing email field.
    """
    data_with_missing_email = SAMPLE_DATA.copy()
    data_with_missing_email[0].pop("email")  # Remove email field
    df = normalize_employee_data(data_with_missing_email)
    assert df['email'].iloc[0] == "Missing", "Missing email not handled correctly"

def test_invalid_hire_date_handling():
    """
    Test to check if invalid hire dates are handled gracefully.
    """
    data_with_invalid_date = SAMPLE_DATA.copy()
    data_with_invalid_date[0]['hire_date'] = "invalid_date"
    df = normalize_employee_data(data_with_invalid_date)
    assert pd.isnull(df['hire_date'].iloc[0]), "Invalid hire date not handled correctly"

def test_full_name_generation():
    """
    Test to verify that the Full Name column is generated correctly.
    """
    df = normalize_employee_data(SAMPLE_DATA)
    assert df['Full Name'].iloc[0] == "John Doe", "Full Name generation failed"
