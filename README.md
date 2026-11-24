This project focuses on cleaning an employee dataset using Python and Pandas.

- Total Rows: 105
- Total Columns: 7
- Missing Values: 55
- Duplicate Rows: 5

1. Loaded the dataset using Pandas.
2. Identified and handled missing values.
3. Converted columns into appropriate data types.
4. Removed duplicate records.
5. Standardized text columns.
6. Detected salary outliers using the IQR method.
7. Capped outlier values.
8. Generated a before-and-after cleaning summary.

- `dataset.csv` – Original dataset
- `clean_data.csv` – Cleaned dataset
- `cleaning_summary.csv` – Cleaning summary

- Python
- Pandas
- NumPy

```bash
python data_cleaning.py
```

- Rows reduced from 105 to 100.
- Duplicate rows reduced from 5 to 0.
- Missing values reduced from 55 to 10.
- Remaining 10 missing Join_Date values are intentionally preserved and flagged.
