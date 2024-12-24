import pandas as pd

# Define a function to calculate total data for an application
def calculate_total_data(df, app_name):
    dl_column = f"{app_name} dl (bytes)"
    ul_column = f"{app_name} ul (bytes)"
    total_column = f"total {app_name} data"
    if dl_column in df.columns and ul_column in df.columns:
        df[total_column] = df[dl_column] + df[ul_column]
    return df

# Aggregation with corrected column names
def aggregate_user_data(df):
    aggregation = {
        'bearer id': 'count',  # Number of xDR sessions
        'dur. (ms)': 'sum',     # Total session duration (in ms)
        'total dl (bytes)': 'sum',  # Total download data
        'total ul (bytes)': 'sum',  # Total upload data
        'social media dl (bytes)': 'sum',
        'social media ul (bytes)': 'sum',
        'youtube dl (bytes)': 'sum',  
        'youtube ul (bytes)': 'sum',
        'netflix dl (bytes)': 'sum',
        'netflix ul (bytes)': 'sum',
        'google dl (bytes)': 'sum',
        'google ul (bytes)': 'sum',
        'email dl (bytes)': 'sum',
        'email ul (bytes)': 'sum',
        'gaming dl (bytes)': 'sum',
        'gaming ul (bytes)': 'sum',
        'other dl (bytes)': 'sum',  
        'other ul (bytes)': 'sum'
    }
    
    # Group and aggregate
    user_aggregates = df.groupby('msisdn/number').agg(aggregation)
    
    # Rename columns for clarity
    user_aggregates.rename(columns={
        'bearer id': 'Number of Sessions',
        'dur. (ms)': 'Total Session Duration (ms)',
        'total dl (bytes)': 'Total Download Data (Bytes)',
        'total ul (bytes)': 'Total Upload Data (Bytes)'
    }, inplace=True)
    
    return user_aggregates

# Define a function to process and calculate application totals
def process_application_totals(user_aggregates,applications):
    for app in applications:
        user_aggregates = calculate_total_data(user_aggregates, app)
    return user_aggregates
