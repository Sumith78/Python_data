import pandas as pd

# Load the complex CSV file into a DataFrame
df = pd.read_csv('complex_employee_details.csv')

# Print the DataFrame to verify its content
print("Original DataFrame:")
print(df)

# 1. Handling Missing Values
# Fill missing salary values with the mean salary
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df = df.dropna(subset=['Department'])
clean_department = df['Department'].dropna()



# Convert the 'PhoneNumber' column to string type (if not already)
df['PhoneNumber'] = df['PhoneNumber'].astype(str)

# Add a new column 'Length' to calculate the length of phone numbers
df['Length'] = df['PhoneNumber'].apply(len)

# Drop rows where the phone number starts with 1, 2, 3, 4, or 5
df = df[~df['PhoneNumber'].str.startswith(('1', '2', '3', '4', '5'))]

# Drop rows where the phone number length is less than 10
df = df[df['Length'] >= 10]

# Drop the 'Length' column as it's no longer needed
df = df.drop(columns=['Length'])

# Fill missing joining dates with a placeholder
df['DateOfJoining'].fillna('Unknown', inplace=True)

# 2. Removing Duplicates
df.drop_duplicates(inplace=True)

# 3. Data Type Conversions
df['DateOfJoining'] = pd.to_datetime(df['DateOfJoining'], errors='coerce')  # Convert to datetime, coerce errors to NaT

# 4. Renaming Columns for Clarity
df.rename(columns={'Experience': 'ExperienceYears'}, inplace=True)

# 5. Removing Unnecessary Columns
# Assuming 'Email' is not needed for further analysis
# df.drop(columns=['Email'], inplace=True)

# 6. Handling Inconsistent Data (e.g., case sensitivity in department names)
df['Department'] = df['Department'].str.title()

# 7. Adding Derived Columns
# Calculate annual bonus as 10% of the salary
df['AnnualBonus'] = df['Salary'] * 0.10

# Print the cleaned and preprocessed DataFrame
print("\nCleaned and Preprocessed DataFrame:")
print(df)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_employee_details.csv', index=False)

print("\nCleaned CSV file 'cleaned_employee_details.csv' created successfully!")
