import matplotlib.pyplot as plt
import seaborn as sbs
import numpy as np

import matplotlib.pyplot as plt

def histogram(data, title='Histogram'):
    # Loop through numeric columns
    numeric_columns = data.select_dtypes(include='number').columns  # Get numeric columns
    for col in numeric_columns:
        plt.figure(figsize=(8, 6))  # Create a new figure with smaller size for each column
        plt.hist(data[col], bins=15, color='skyblue', edgecolor='black')  # Plot histogram
        plt.title(f"{title} - {col}")  # Title with column name
        plt.xlabel(col)  # Label x-axis with column name
        plt.ylabel('Frequency')  # Label y-axis
        
        plt.tight_layout()  # Adjust the layout to prevent overlap
        plt.show()  # Show the plot

def boxplot(data, title='Boxplot'):
    sbs.boxplot(x=data)
    plt.title(title)
    plt.show()

def scatter_plot(x, y, title='Scatter Plot'):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def correlation_heatmap(dataframe, title='Correlation Heatmap'):
    sbs.heatmap(dataframe.corr(), annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()



