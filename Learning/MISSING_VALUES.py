import pandas as pd
import numpy as np

data={
    'department': ['IT','Sales',None,'Marketing',None,'Product'],
    'Salary':[50000,15000,10000,16000,35000,500000]
}

df=pd.DataFrame(data)

print(f"Original Data:\n {df}")


df=df.dropna(subset=['department'])
print(f"\n Filtered Department After dropping Nan values: \n {df}")


Cleaned_Data=df['department'].dropna()
print(f"\n Department Names without Nan Values: \n {Cleaned_Data}")