import numpy as np
import pandas as pd

def transform_data(data):
    """Transforms the data by creating new features or modifying existing ones."""
    print("Transforming data...")

    # Example transformation: Convert a column from bytes to megabytes
    if 'size_in_bytes' in data.columns:
        data['size_in_mb'] = data['size_in_bytes'] / (1024 * 1024)

    # Example transformation: Create a new column (e.g., log transformation)
    
    if 'value_column' in data.columns:
        data['log_value'] = np.log1p(data['value_column'])

    print("Data transformation completed.")
    return data

def compute_total_duration(df):
    """Compute the total duration for all sessions per user."""
    df['total_duration'] = df.groupby('msisdn/number')['dur. (ms)'].transform('sum')
    return df

def create_decile_classes(df):
    """Create decile classes based on total session duration."""
    valid_users = df[df['total_duration'].notnull()].copy()  # Use .copy() to avoid the warning
    valid_users['duration_decile'] = pd.qcut(valid_users['total_duration'], 10, labels=False, duplicates='drop')
    return valid_users

def compute_total_data_per_decile(valid_users):
    """Compute total data (DL + UL) per decile class."""
    valid_users = valid_users.copy()  # Ensure valid_users is a copy to avoid the warning
    valid_users['total_data'] = valid_users['total dl (bytes)'] + valid_users['total ul (bytes)']
    decile_analysis = valid_users.groupby('duration_decile').agg({
        'total_data': 'sum',
        'total_duration': 'mean',  # Optional: Average duration per decile
        'msisdn/number': 'nunique'  # Optional: Number of users in each decile
    }).rename(columns={
        'total_data': 'Total Data (Bytes)',
        'total_duration': 'Average Duration (ms)',
        'msisdn/number': 'User Count'
    })
    return decile_analysis
