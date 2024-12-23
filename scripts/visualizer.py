import matplotlib.pyplot as plt

def uni_variate_plot(data, column, title, xlabel, ylabel, color):
    plt.plot(data[column], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def bi_variate_plot(data, column1, column2, title, xlabel, ylabel, color):
    plt.scatter(data[column1], data[column2], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_histogram(data, column, bins, title, xlabel, ylabel, color, kde=False):
    plt.hist(data[column], bins=bins, color=color, edgecolor='black', density=kde)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()