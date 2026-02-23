#!/usr/bin/env python3
"""
Data cleaning script for ML pipeline component.
Demonstrates containerized data processing.
"""

import pandas as pd
import sys
from pathlib import Path


def clean_data(input_file: str, output_file: str):
    """
    Clean data by handling missing values, removing duplicates, and standardizing types.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to save cleaned CSV file
    """
    print(f"📂 Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    print(f"📊 Original dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\n🔍 Data types:\n{df.dtypes}\n")
    
    # Display missing values
    missing = df.isnull().sum()
    if missing.any():
        print(f"⚠️  Missing values found:\n{missing[missing > 0]}\n")
    
    # Clean data
    print("🧹 Cleaning data...")
    
    # 1. Remove duplicate rows
    original_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = original_rows - len(df)
    if duplicates_removed > 0:
        print(f"   ✓ Removed {duplicates_removed} duplicate rows")
    
    # 2. Handle missing values (drop rows with any missing values)
    rows_before = len(df)
    df = df.dropna()
    rows_dropped = rows_before - len(df)
    if rows_dropped > 0:
        print(f"   ✓ Removed {rows_dropped} rows with missing values")
    
    # 3. Strip whitespace from string columns
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].str.strip()
    if len(string_cols) > 0:
        print(f"   ✓ Stripped whitespace from {len(string_cols)} text columns")
    
    # 4. Convert numeric columns that might have been read as strings
    for col in df.columns:
        try:
            # Try to convert to numeric
            df[col] = pd.to_numeric(df[col])
        except (ValueError, TypeError):
            # If it fails, keep original type
            pass
    
    print(f"\n✅ Cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Save cleaned data
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"💾 Cleaned data saved to {output_file}")
    
    # Display sample
    print(f"\n📋 Sample of cleaned data:\n{df.head()}\n")
    
    # Display basic statistics
    print(f"📈 Summary statistics:\n{df.describe()}\n")


if __name__ == "__main__":
    # Default file paths
    input_file = "/data/input/raw_data.csv"
    output_file = "/data/output/cleaned_data.csv"
    
    # Allow command line arguments to override defaults
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        clean_data(input_file, output_file)
        print("🎉 Data cleaning completed successfully!")
    except FileNotFoundError:
        print(f"❌ Error: Could not find input file '{input_file}'")
        print("   Make sure you've mounted the data directory with -v flag")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
