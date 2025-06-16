# Employee Data Scraper

This project is a Python-based scraper designed to fetch, process, and normalize employee data from the API endpoint: [https://api.slingacademy.com/v1/sample-data/files/employees.json](https://api.slingacademy.com/v1/sample-data/files/employees.json). The processed data is saved in a clean format suitable for ingestion into a data warehouse.

## Features

### 1. **Data Retrieval**
- Fetches employee data via an HTTP GET request.
- Handles API response errors (e.g., non-200 status codes, timeouts) with retries and appropriate logging.

### 2. **Data Structure Validation**
- Extracts essential fields:
  - Employee ID
  - First Name
  - Last Name
  - Email
  - Job Title
  - Phone Number
  - Hire Date
- Ensures all extracted fields match the expected schema.

### 3. **Data Normalization**
- **New Columns:**
  - `Full Name`: Combines "First Name" and "Last Name."
  - `Designation`: Categorized based on `years_of_experience`:
    - `<3 years`: System Engineer
    - `3-5 years`: Data Engineer
    - `5-10 years`: Senior Data Engineer
    - `10+ years`: Lead
- **Phone Validation:** Marks numbers containing 'x' as "Invalid Number."
- **Consistent Data Types:**
  - `Full Name`: string
  - `email`: string
  - `phone`: int
  - `gender`: string
  - `age`: int
  - `job_title`: string
  - `years_of_experience`: int
  - `salary`: int
  - `department`: string
- **Date Formatting:** Ensures `hire_date` is in the format `YYYY-MM-DD`.

### 4. **Error Handling**
- Logs detailed error messages for failed requests.
- Retries a limited number of times for connection issues.

### 5. **Optional Enhancements**
- **Currency Conversion:** Mechanism to standardize salary into a single currency (using an external API).
- **Extensibility:** Additional processing and normalization rules can be easily added.

## Installation

### Prerequisites
- Python 3.10 or higher
- `pip` for package management

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/employee-data-scraper.git
   cd employee-data-scraper
   ````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper:

   ```bash
   python employee_scraper.py
   ```
2. The normalized data will be saved as `employee_data.csv` in the project directory.

## Testing

### Run Unit Tests

Execute the following command to run the test suite:

```bash
pytest test_employee_scraper.py
```

### Test Cases

1. **Verify JSON File Download:** Ensures successful data retrieval.
2. **Verify JSON File Extraction:** Tests correct parsing of JSON fields.
3. **Validate File Type and Format:** Ensures normalized data saves as a valid CSV.
4. **Validate Data Structure:** Confirms all required fields and data types.
5. **Handle Missing or Invalid Data:** Tests for graceful handling of anomalies.

## File Structure

```plaintext
employee-data-scraper/
├── employee_scraper.py          # Main scraper logic
├── data_normalization.py        # Normalization functions
├── test_employee_scraper.py     # Test suite
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── employee_data.csv            # Output file (generated)
```

## Contributions

Contributions are welcome! Please create an issue or submit a pull request for any feature requests or bug fixes.

## Author

**Joanna Leticia Pinto**
Bachelor's in Artificial Intelligence and Data Science
NMAM Institute of Technology


