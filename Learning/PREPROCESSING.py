import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, 30],
    'Salary': [50000, 60000, np.nan, 80000, 75000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

# Handle missing data
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Encode categorical data
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Feature scaling
# scaler = StandardScaler()
# df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# Remove duplicates
df = df.drop_duplicates()

# Check final DataFrame
print(df)
