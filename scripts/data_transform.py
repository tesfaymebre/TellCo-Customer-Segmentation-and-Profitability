import numpy as np

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