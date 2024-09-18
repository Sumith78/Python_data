import pandas as pd
import numpy as np

# Sample data with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, np.nan],
    'Salary': [50000, 60000, np.nan, 80000, 75000],
    'Department': ['HR', 'IT', 'HR', np.nan, 'IT']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Handling missing values
# 1. Fill missing values in 'Age' with the mean of the column
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 2. Fill missing values in 'Salary' with the median of the column
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# 3. Fill missing values in 'Department' with the mode of the column
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

# Check the DataFrame after handling missing values
print("\nDataFrame after handling missing values:")
print(df)
