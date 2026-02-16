"""
Data Quality Profiler
A utility to analyze CSV files and generate data quality reports.

This module provides functions to profile datasets and identify potential
data quality issues commonly encountered in ML pipelines.
"""

from typing import Dict, List, Tuple, Optional, Any
import pandas as pd
import json
from pathlib import Path

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file into/as a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file to load.
        
    Returns:
        (pd.DataFrame): DataFrame containing the loaded data.
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError(f"File is empty: {filepath}")
    
    return df

