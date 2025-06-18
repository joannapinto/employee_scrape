import pandas as pd
import requests

def fetch_employee_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def normalize_employee_data(data):
    df = pd.DataFrame(data)
    expected_columns = ['first_name', 'last_name', 'phone', 'email', 'gender', 
                        'age', 'job_title', 'years_of_experience', 'salary', 
                        'department', 'hire_date']
    for col in expected_columns:
        if col not in df.columns:
            df[col] = None

    # Handle missing last names
    df['last_name'] = df['last_name'].fillna("Missing")

    # Handle invalid phone numbers
    df['phone'] = df['phone'].apply(lambda x: "Invalid Number" if not str(x).isdigit() else x)

    # Add a Full Name column
    df['Full Name'] = (df['first_name'] + ' ' + df['last_name']).astype("string")

    # Convert salary to float
    df['salary'] = df['salary'].fillna(0).astype(float)

    # Convert hire_date to datetime
    df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

    # Assign designation based on years of experience
    df['designation'] = pd.cut(df['years_of_experience'],
                                bins=[-1, 3, 5, 10, float('inf')],
                                labels=["System Engineer", "Senior Data Engineer", "Lead Engineer", "Principal Engineer"],
                                include_lowest=True,
                                right=True)

    return df

if __name__ == "__main__":
    API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"
    try:
        raw_data = fetch_employee_data(API_URL)
        normalized_data = normalize_employee_data(raw_data)
        normalized_data.to_json("employees.json", orient="records", indent=4, date_format="iso")
        print("Data saved to employees.json")
    except Exception as e:
        print(f"An error occurred: {e}")
