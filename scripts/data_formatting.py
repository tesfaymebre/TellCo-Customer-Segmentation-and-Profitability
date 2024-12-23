import pandas as pd

def format_data(data):
    """Formats the data for final export."""
    print("Formatting data...")

    # Rename columns for clarity
    data = data.rename(columns={
        'old_column_name': 'new_column_name',
        'size_in_mb': 'size_in_megabytes'
    })

    # Ensure date column is in standard format
    if 'date_column' in data.columns:
        data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')

    print("Data formatting completed.")
    return data