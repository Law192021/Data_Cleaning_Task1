import pandas as pd
df = pd.read_csv("data/dataset.csv")
original_rows = len(df)
original_missing = df.isnull().sum().sum()
original_duplicates = df.duplicated().sum()

print("BEFORE CLEANING")
print("Rows:", original_rows)
print("Missing Values:", original_missing)
print("Duplicates:", original_duplicates)

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)
df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

# Join_Date - Leave and flag
df["Join_Date_Missing"] = df["Join_Date"].isna()

print("\nMISSING VALUES AFTER HANDLING")
print(df.isnull().sum())


df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

df["Join_Date"] = pd.to_datetime(
    df["Join_Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

df["Department"] = df["Department"].astype("category")
df["City"] = df["City"].astype("category")

print("\nDATA TYPES")
print(df.dtypes)

df = df.drop_duplicates()

print("\nDUPLICATES AFTER CLEANING")
print(df.duplicated().sum())

df["Name"] = (
    df["Name"]
    .astype("string")
    .str.strip()
    .str.title()
)

df["Department"] = (
    df["Department"]
    .astype("string")
    .str.strip()
    .str.title()
    .astype("category")
)

df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.title()
    .astype("category")
)

print("\nSTANDARDIZED TEXT")
print(df[["Name", "Department", "City"]].head())

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\nOUTLIER DETECTION")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

df["Salary_Outlier"] = (
    (df["Salary"] < lower_bound) |
    (df["Salary"] > upper_bound)
)

print("Total Outliers:", df["Salary_Outlier"].sum())

df["Salary"] = df["Salary"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\nAFTER OUTLIER HANDLING")
print("Maximum Salary:", df["Salary"].max())
cleaned_rows = len(df)
cleaned_missing = df.isnull().sum().sum()
cleaned_duplicates = df.duplicated().sum()
summary = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Missing Values",
        "Duplicate Rows"
    ],
    "Before Cleaning": [
        original_rows,
        original_missing,
        original_duplicates
    ],
    "After Cleaning": [
        cleaned_rows,
        cleaned_missing,
        cleaned_duplicates
    ]
})
print("\nBEFORE AND AFTER CLEANING SUMMARY")
print(summary.to_string(index=False))
df.to_csv("data/clean_data.csv", index=False)
summary.to_csv("data/cleaning_summary.csv", index=False)
print("\nCleaned dataset saved successfully!")
print("Summary saved successfully!")
