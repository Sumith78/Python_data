import pandas as pd

# Sample DataFrame
Data = {
    'Name': ['Sumith', 'Rohith', 'Sumith', 'Shubham', 'Rohith', 'Gagan'],
    'Department': ['Hr', 'IT', 'Hr', 'Hr', 'IT', 'Sales'],
    'Salary': [50000, 15000, 25000, 65000, 45000, 100000]
}

df = pd.DataFrame(Data)
print(f"Original Data: \n{df}")

# Step 1: Filter rows where 'Department' is 'Hr' and drop duplicates based on 'Name'
df_hr = df[df['Department'] == 'Hr'].drop_duplicates(subset=['Name'], keep='first')

# Step 2: Get rows where 'Department' is not 'Hr'
df_non_hr = df[df['Department'] != 'Hr']

# Step 3: Combine the filtered 'Hr' department rows and the non-Hr department rows
df_cleaned = pd.concat([df_hr, df_non_hr], ignore_index=True)

print(f"\nDataFrame after removing duplicate names where Department is 'Hr':\n{df_cleaned}")












# import pandas as pd

# # Sample DataFrame
# Data = {
#     'Name': ['Sumith', 'Rohith', 'Sumith', 'Shubham', 'Rohith', 'Gagan'],
#     'Department': ['Hr', 'IT', 'Hr', 'Hr', 'IT', 'Sales'],
#     'Salary': [50000, 15000, 25000, 65000, 45000, 100000]
# }

# df = pd.DataFrame(Data)
# print(f"Original Data: \n{df}")

# # Drop rows where both 'Name' and 'Department' are duplicated
# df_cleaned = df.drop_duplicates(subset=['Name', 'Department'], keep=False)

# print(f"\nDataFrame after removing rows where both 'Name' and 'Department' are duplicates:\n{df_cleaned}")



