## Data Storage

### Folder Structure
- `data/raw/` : contains raw data files directly from sources (CSV format).
- `data/processed/` : contains processed data, ready for analysis (Parquet format if engine available).

### File Formats
- **CSV**: human-readable, easy to inspect, universally supported.
- **Parquet**: columnar, efficient for storage and fast reads, requires `pyarrow` or `fastparquet`.

### How Code Reads/Writes Data
- Environment variables from `.env` control folder paths:
  ```text
  DATA_DIR_RAW=data/raw
  DATA_DIR_PROCESSED=data/processed

