import pandas as pd

data = {'A': [1, 2, None], 'B': [4, None, 6]}
df = pd.DataFrame(data)

df_filled = df.fillna(0).astype(int)
df_dropped = df.dropna().astype(int)


# Uses fillna(0) to fill the None values with 0,
# creating df_filled.
# Uses dropna() to drop any rows with None values, creating df_dropped.

print(df_filled)
print("")
print(df_dropped)


# What is a DataFrame?
# Structure: A DataFrame consists of rows and columns, much like an Excel spreadsheet or a SQL table. Each column can contain different types of data (e.g., integers, strings, floating-point numbers).
# Labeled Axes: Each row and each column in a DataFrame is labeled. The row labels are called the index, and the column labels are the column names.
# Size-Mutable: You can add or remove rows and columns.
# Data Alignment: DataFrames automatically align data for arithmetic operations based on labels.
