import numpy as np
import pandas as pd

def clean_data(data, critical_columns):
    """
    Cleans and preprocesses the dataset.
    
    Steps:
    - Drop duplicates
    - Handle missing values
    - Treat outliers
    """
    print("Starting data cleaning...")
    
    # Step 1: Drop duplicates
    data = data.drop_duplicates()

    # Step 2: Handle missing critical data (e.g., unique identifiers)
    data = data.dropna(subset=critical_columns, how='any')

    # Step 3: Fill missing values for numeric columns with the column mean
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean(numeric_only=True))

    # Step 4: Fill missing non-critical categorical columns with a default value
    categorical_columns = data.select_dtypes(include=['object']).columns
    data[categorical_columns] = data[categorical_columns].fillna("unknown")

    print("Missing value handling completed.")
    
    # Step 5: Treat outliers
    for column in numeric_columns:
        data[column] = treat_outliers_with_mean(data[column])
    
    print("Outlier treatment completed.")
    print("Data cleaning finished.")
    return data

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
    return np.where((column < lower_bound) | (column > upper_bound), column_mean, column)

def missing_value_report(data):
    """
    Generates a report of missing values in the dataset.
    
    Args:
        data: The DataFrame to analyze.

    Returns:
        A DataFrame showing columns with missing values and their counts.
    """
    missing_values = data.isnull().sum()
    missing_report = missing_values[missing_values > 0].sort_values(ascending=False)
    return pd.DataFrame({
        "Column": missing_report.index,
        "Missing Values": missing_report.values,
        "Percentage": (missing_report.values / len(data)) * 100
    })

# Grouped median imputation
def impute_missing_values(df, group_column, value_column):
    """
    Imputes missing values in a DataFrame using grouped median imputation.

    Args:
        df: The input DataFrame.
        group_column: The column used for grouping.
        value_column: The column to impute.

    Returns:
        The DataFrame with missing values imputed.
    """
    df[value_column] = df.groupby(group_column)[value_column].transform(lambda x: x.fillna(x.median()))
    return df