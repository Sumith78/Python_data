import pandas as pd
import numpy as np

# Create a dictionary with more complex employee details
data = {
    'EmployeeID': np.arange(1001, 1101),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Judy'] * 10,
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'HR', 'Finance', 'IT', 'Marketing', 'Sales'] * 10,
    'Position': ['Manager', 'Analyst', 'Developer', 'Executive', 'Representative', 'Assistant', 'Consultant', 'Lead', 'Coordinator', 'Specialist'] * 10,
    'Salary': [60000, 55000, 70000, 50000, 45000, 52000, 58000, 75000, 49000, 47000] * 10,
    'DateOfJoining': pd.date_range(start='1/1/2010', periods=100, freq='M').strftime('%Y-%m-%d').tolist(),
    'Experience': [5, 3, 8, 2, 1, 4, 7, 9, 2, 1] * 10,
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eva@example.com',
              'frank@example.com', 'grace@example.com', 'hannah@example.com', 'ivan@example.com', 'judy@example.com'] * 10,
    'PhoneNumber': ['1234567890', '2345678901', '3456789012', '4567890123', '5678901234',
                    '6789012345', '7890123456', '8901234567', '9012345678', '0123456789'] * 10
}

# Introduce some inconsistencies and missing values
data['Salary'][5] = None  # Missing salary for one employee
data['Email'][15] = 'charlie@com'  # Incorrect email format
data['PhoneNumber'][25] = '12345'  # Incomplete phone number
data['Department'][35] = None  # Missing department for one employee
data['Experience'][45] = -1  # Negative experience value

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('complex_employee_details.csv', index=False)

print("CSV file 'complex_employee_details.csv' created successfully!")
