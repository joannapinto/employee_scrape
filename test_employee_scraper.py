import unittest
from unittest.mock import patch, Mock
import pandas as pd
from employee_scraper import fetch_employee_data, normalize_employee_data

# Mock API response
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

class TestEmployeeScraper(unittest.TestCase):

    @patch('employee_scraper.requests.get')
    def test_fetch_employee_data_success(self, mock_get):
        """
        Test Case: Successful API request
        """
        # Configure the mock to return a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_API_RESPONSE
        mock_get.return_value = mock_response

        data = fetch_employee_data("https://api.slingacademy.com/v1/sample-data/files/employees.json")
        self.assertEqual(data, MOCK_API_RESPONSE, "Failed to fetch correct employee data.")

    @patch('employee_scraper.requests.get')
    def test_fetch_employee_data_failure(self, mock_get):
        """
        Test Case: Failed API request (non-200 status)
        """
        # Configure the mock to return a failed response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            fetch_employee_data("https://api.slingacademy.com/v1/sample-data/files/employees.json")
        self.assertIn("Failed to fetch data", str(context.exception), "Failed to raise exception on API failure.")

    def test_normalize_employee_data(self):
        """
        Test Case: Validate normalization logic.
        """
        df = normalize_employee_data(MOCK_API_RESPONSE)
        self.assertIn("Full Name", df.columns, "Full Name column is missing.")
        self.assertIn("designation", df.columns, "Designation column is missing.")
        self.assertEqual(df['designation'].iloc[0], "Senior Data Engineer", "Designation assignment is incorrect.")

    def test_handle_missing_or_invalid_data(self):
        """
        Test Case: Handle missing or invalid data.
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
        self.assertEqual(df['last_name'].iloc[0], "Missing", "Missing last name not handled correctly.")
        self.assertEqual(df['phone'].iloc[0], "Invalid Number", "Invalid phone not handled correctly.")

if __name__ == "__main__":
    unittest.main()
