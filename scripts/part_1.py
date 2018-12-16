import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

sns.set(style="whitegrid")


def load_data(filepath):
    """
    Given a path to a CSV file, this function reads that file as a dataframe using Pandas.
    """
    return pd.read_csv(filepath)


def print_value_counts(df):
    """
    Given a dataframe, this function goes through the data type of all columns,
    and if the column is of type 'object', print the counts of each unique value in the column.

    Note: not all categorical columns are captured by the 'object' data type. This function
          can be edited to also accept a list of columns to print the value counts for.
    """
    # for each column in the data types list
    for column in df.dtypes.index:
        # if the column is of type object (i.e. categorical)
        if df.dtypes[column] == 'object':
            # count the values and print them
            print(df[column].value_counts())
            print("\n\n")


def print_table(df):
    """
    Prints a dataframe using the `tabulate` library to print a table into the console.
    """
    print(tabulate(df, headers="keys" , tablefmt="orgtbl"))


def plot_value_counts(df, column, title='Value Counts Plot'):
    """
    Create a barplot for the value counts of a specific column using Seaborn library.
    """
    counts = df[column].value_counts()
    ax = sns.barplot(x=counts.index, y=counts.values)
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.title(title)
    plt.show(ax)


def boxplot(df, x, y=None, hue=None, title='Boxplot'):
    """
    Create a box plot for a single column or 2 columns compared against each other.
    """
    ax = sns.boxplot(x=x, y=y, hue=hue, data=df)
    plt.title(title)
    plt.show(ax)


if __name__ == '__main__':
    # load the data from a CSV file
    data = load_data('data/student-data.csv')
    
    # print the descriptive statistics
    print("Some quick stats:")
    print(data.describe().round(2))
    print("")
    
    # show a boxplot of 'age' in 2 groups (passed or not)
    boxplot(data, x='age', y='passed', title='Age vs. Passed - Boxplot')

    # show a boxplot of 'age' in 2 groups (passed or not)
    boxplot(data, x='age', y='passed', title='Age vs. Passed - Boxplot')
