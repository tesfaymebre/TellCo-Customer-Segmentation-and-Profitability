import pandas as pd

# Define a function to describe variables and data types
def describe_variables(df):
    variable_summary = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes,
        "Unique Values": [df[col].nunique() for col in df.columns],
        "Missing Values": df.isnull().sum()
    })
    return variable_summary

def calculate_dispersion_parameters(df):
    """
    Calculate dispersion parameters for a given DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing numeric data.
    
    Returns:
    pd.DataFrame: DataFrame containing dispersion parameters.
    """
    
    # Ensure the DataFrame contains only numeric data
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    dispersion_analysis = numeric_df.describe().T
    dispersion_analysis['Range'] = dispersion_analysis['max'] - dispersion_analysis['min']
    dispersion_analysis['Variance'] = numeric_df.var()
    
    return dispersion_analysis

def save_to_csv(data, file_path, index=True):
    """
    Save the data parameters to a CSV file.
    
    Parameters:
    data (pd.DataFrame): DataFrame to save.
    file_path (str): Path to save the CSV file.
    """
    data.to_csv(file_path, index=index)