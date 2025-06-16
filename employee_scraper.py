import pandas as pd

def normalize_employee_data(data):
    """
    Normalizes the given employee data and returns a pandas DataFrame.
    """
    print("Normalizing data...")
    
    # Convert input data to a DataFrame
    df = pd.DataFrame(data)

    # Ensure all expected columns are present
    expected_columns = ['first_name', 'last_name', 'phone', 'email', 'gender', 
                        'age', 'salary', 'department', 'hire_date', 'designation']
    for col in expected_columns:
        if col not in df.columns:
            # Default values for missing columns
            df[col] = 'Missing' if col not in ['age', 'salary'] else 0

    # Add a Full Name column
    df['Full Name'] = df['first_name'] + ' ' + df['last_name']

    # Normalize data types
    df = df.astype({
        'first_name': 'string',
        'last_name': 'string',
        'phone': 'string',
        'email': 'string',
        'gender': 'string',
        'age': 'int',
        'salary': 'float',
        'department': 'string',
        'hire_date': 'string',
        'designation': 'string',
        'Full Name': 'string'
    })

    # Handle missing or invalid data
    df['gender'] = df['gender'].replace({'': 'Unknown', None: 'Unknown'})
    df['phone'] = df['phone'].fillna('Unknown')
    df['email'] = df['email'].fillna('Missing')
    df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')  # Handle invalid dates

    print("Normalization process completed.")
    return df


if __name__ == "__main__":
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
    try:
        df = normalize_employee_data(SAMPLE_DATA)
        print(df)
        df.to_csv("normalized_data.csv", index=False)
        print("Data saved to normalized_data.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
