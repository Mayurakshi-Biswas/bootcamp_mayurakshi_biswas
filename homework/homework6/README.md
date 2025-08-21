# Homework 6: Data Cleaning

## Cleaning Strategy

1. **fill_missing_median()** — fills missing numeric values with the median of the column.
2. **drop_missing()** — drops rows with too many missing values (threshold applied).
3. **normalize_data()** — scales numeric columns to a 0-1 range.

## Folder Structure

- `data/raw/` — original dataset CSV
- `data/processed/` — cleaned dataset CSV
- `src/` — contains cleaning.py with reusable functions
- `notebooks/` — Jupyter notebook demonstrating cleaning workflow

## Assumptions

- Median is used for filling numeric columns.
- Threshold for dropping missing rows is 50% by default.
- Only numeric columns are normalized.

