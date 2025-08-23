import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    """Fill missing values in specified columns with the median."""
    for col in columns:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    return df

def drop_missing(df, threshold=0.5):
    """
    Drop rows with missing values above the threshold.
    threshold: fraction of allowed missing columns per row.
    """
    return df[df.isnull().mean(axis=1) <= threshold]

def normalize_data(df, columns):
    """Normalize numeric columns to 0-1 range."""
    for col in columns:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if pd.notnull(min_val) and max_val != min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df

    
