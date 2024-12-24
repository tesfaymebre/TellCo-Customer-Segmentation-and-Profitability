import matplotlib.pyplot as plt
import seaborn as sns

def uni_variate_plot(data, column, title, xlabel, ylabel, color):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True, bins=30, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def bi_variate_plot(data, column1, column2, title, xlabel, ylabel, color):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=column1, y=column2, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Analyze relationships between applications and total data
def bi_variate_plot2(df, applications):
    """
    Function to analyze relationships between applications and total data.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    applications (list): List of application names to analyze.
    
    Returns:
    None
    """
    sns.pairplot(df, vars=[f'total {app} data' for app in applications])
    plt.suptitle("Bivariate Analysis of Applications and Total Data")
    plt.show()

def plot_histogram(data, column, bins, title, xlabel, ylabel, color, kde=False):
    plt.hist(data[column], bins=bins, color=color, edgecolor='black', density=kde)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# correlation matrix
def plot_correlation_matrix(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=2)
    plt.title('Correlation Matrix')
    plt.show()