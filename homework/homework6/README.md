
## Cleaning Strategy

In this homework, we implemented reusable data cleaning functions and applied them to a raw dataset.

### 1. Functions

- **fill_missing_median(df, columns)**  
  Fills missing values in specified numeric columns with the median of each column.

- **drop_missing(df, threshold=0.5)**  
  Drops rows where the fraction of missing columns exceeds the threshold.

- **normalize_data(df, columns)**  
  Normalizes numeric columns to a 0-1 range.

### 2. Notebook Workflow

1. Load the raw dataset from `data/raw/sample_data.csv`.
2. Apply the cleaning functions in the following order:
   - Fill missing values with median
   - Drop rows with excessive missing values
   - Normalize numeric columns
3. Save the cleaned dataset to `data/processed/sample_data_cleaned.csv`.
4. Compare original vs cleaned dataset in the notebook.

### 3. Assumptions

- Only numeric columns (`age`, `income`, `score`, `extra_data`) are normalized.
- Missing values are handled via median imputation for numeric columns; rows with >50% missing are dropped.
- Non-numeric columns (`zipcode`, `city`) are preserved as-is.

### 4. Reproducibility

- All scripts are modular under `src/cleaning.py`.
- Notebook can be rerun independently to reproduce cleaned dataset.
- Data directories are structured to separate raw and processed data.


