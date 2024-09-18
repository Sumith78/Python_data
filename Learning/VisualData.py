import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(0)
data = {
    'Age': [25, np.nan, 35, 40, np.nan, 45, 50, np.nan, 55, 60],
    'Salary': [50000, 60000, np.nan, 80000, 75000, np.nan, 95000, 100000, np.nan, 105000]
}

df = pd.DataFrame(data)

# Plot original data
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(df['Age'], bins=5, ax=axes[0], kde=True, color='blue', label='Original')
sns.histplot(df['Salary'], bins=5, ax=axes[1], kde=True, color='green', label='Original')

axes[0].set_title('Original Age Distribution')
axes[1].set_title('Original Salary Distribution')

plt.legend()
plt.show()

# Handling missing values
df['Age_mean_filled'] = df['Age'].fillna(df['Age'].mean())
df['Salary_median_filled'] = df['Salary'].fillna(df['Salary'].median())
df['Department_mode_filled'] = df['Department'].fillna(df['Department'].mode()[0])

# Plot data after handling missing values
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.histplot(df['Age_mean_filled'], bins=5, ax=axes[0], kde=True, color='blue', label='Mean Filled')
sns.histplot(df['Salary_median_filled'], bins=5, ax=axes[1], kde=True, color='green', label='Median Filled')
sns.histplot(df['Department_mode_filled'], bins=5, ax=axes[2], kde=True, color='orange', label='Mode Filled')

axes[0].set_title('Age Distribution (Mean Filled)')
axes[1].set_title('Salary Distribution (Median Filled)')
axes[2].set_title('Department Distribution (Mode Filled)')

plt.legend()
plt.show()
