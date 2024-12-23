import numpy as np

def clean_data_1(data):
    """Cleans the extracted data."""
    print("Cleaning data...")

    # Drop duplicates
    data = data.drop_duplicates()

    # Handle missing values (remove rows with missing critical data)
    data = data.dropna(subset=['column_of_interest'], how='any')

    # Fill missing values in other columns with defaults
    data.fillna({'default_column': 0}, inplace=True)

    print("Data cleaning completed.")
    return data

def clean_data_2(data):
    # Step 1: Handle Missing Values - Fill missing numerical values with column mean
    data.fillna(data.mean(numeric_only=True), inplace=True)

def treat_outliers_with_mean(column):
    """
    Detects and replaces outliers in a given column using the IQR method.

    Args:
        column: The column containing the data to be cleaned.

    Returns:
        The cleaned column with outliers replaced by the column mean.
    """

    Q1 = column.quantile(0.25)  # 25th percentile
    Q3 = column.quantile(0.75)  # 75th percentile

    IQR = Q3 - Q1  # Interquartile range

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Replace outliers with the mean
    column_mean = column.mean()
    column = np.where((column < lower_bound) | (column > upper_bound), column_mean, column)

    return column