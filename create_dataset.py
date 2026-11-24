import pandas as pd
import os
data = {
    "Employee_ID": list(range(1, 101)),
    "Name": [
        f" Employee_{i} " if i % 2 == 0 else f"employee_{i}"
        for i in range(1, 101)
    ],
    "Age": [str(20 + (i % 35)) for i in range(1, 101)],
    "Salary": [str(25000 + (i * 500)) for i in range(1, 101)],
    "Department": [
        ["IT", "HR", "Finance", "Sales"][i % 4]
        for i in range(1, 101)
    ],
    "Join_Date": [
        f"{(i % 28) + 1:02d}-01-2024"
        for i in range(1, 101)
    ],
    "City": [
        ["Chennai", "Madurai", "Coimbatore", "Trichy"][i % 4]
        for i in range(1, 101)
    ]
}
df = pd.DataFrame(data)
df.loc[0:9, "Age"] = None
df.loc[10:19, "Salary"] = None
df.loc[20:29, "Department"] = None
df.loc[30:39, "City"] = None
df.loc[40:49, "Join_Date"] = None
df.loc[50, "Salary"] = "999999"
df = pd.concat([df, df.iloc[0:5]], ignore_index=True)
os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False)
print("Sample dataset created successfully!")
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
print("\nDataset Preview:")
print(df.head(10))
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())