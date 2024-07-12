import pandas as pd

# Load the complex CSV file into a DataFrame
df = pd.read_csv('complex_employee_details.csv')

# Save the DataFrame to an Excel file
df.to_excel('employee_details.xlsx', index=False)

print("Excel file 'employee_details.xlsx' created successfully!")
