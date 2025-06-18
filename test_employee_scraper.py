import pytest
import pandas as pd
from employee_scraper import normalize_employee_data

# Mock API response for testing
MOCK_API_RESPONSE = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "12345",
        "email": "john.doe@example.com",
        "gender": "Male",
        "age": 30,
        "job_title": "Engineer",
        "years_of_experience": 5,
        "salary": 75000,
        "department": "Engineering",
        "hire_date": "2023-01-15"
    }
]

def test_normalize_employee_data_columns():
    """
    Test Case 1: Verify all required columns are present.
    """
    df = normalize_employee_data(MOCK_API_RESPONSE)
    expected_columns = ['first_name', 'last_name', 'phone', 'email', 'gender', 'age',
                        'job_title', 'years_of_experience', 'salary', 'department',
                        'hire_date', 'Full Name', 'designation']
    assert all(col in df.columns for col in expected_columns), "Not all required columns are present."

def test_normalize_employee_data_no_missing():
    """
    Test Case 2: Verify no required column has missing values after normalization.
    """
    df = normalize_employee_data(MOCK_API_RESPONSE)
    assert df.isnull().sum().sum() == 0, "Missing values exist in normalized data."

def test_normalize_employee_data_types():
    """
    Test Case 3: Validate column types after normalization.
    """
    df = normalize_employee_data(MOCK_API_RESPONSE)
    assert df.dtypes['Full Name'] == 'string', "Full Name column type is incorrect"
    assert df.dtypes['age'] == 'int64', "Age column type is incorrect"
    assert df.dtypes['salary'] == 'float64', "Salary column type is incorrect"

def test_designation_assignment():
    """
    Test Case 4: Validate designation assignment based on years of experience.
    """
    df = normalize_employee_data(MOCK_API_RESPONSE)
    assert df['designation'].iloc[0] == "Senior Data Engineer", "Designation assignment is incorrect for 5 years of experience"

def test_missing_or_invalid_data_handling():
    """
    Test Case 5: Handle missing or invalid data.
    """
    data_with_issues = [
        {
            "first_name": "Alice",
            "last_name": None,  # Missing last name
            "phone": "123x456",  # Invalid phone
            "email": None,  # Missing email
            "gender": "",
            "age": None,  # Missing age
            "job_title": None,  # Missing job title
            "years_of_experience": 15,
            "salary": None,  # Missing salary
            "department": None,  # Missing department
            "hire_date": "invalid_date"  # Invalid date
        }
    ]
    df = normalize_employee_data(data_with_issues)
    assert df['last_name'].iloc[0] == "Missing", "Missing last name not handled correctly"
    assert df['phone'].iloc[0] == "Invalid Number", "Invalid phone not handled correctly"
