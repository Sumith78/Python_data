import pandas as pd

# Create a dictionary with employee details
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
    'Position': ['Manager', 'Analyst', 'Developer', 'Executive', 'Representative'],
    'Salary': [60000, 55000, 70000, 50000, 45000]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('employee_details.csv', index=False)

print("CSV file 'employee_details.csv' created successfully!")
