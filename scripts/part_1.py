import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

sns.set(style="whitegrid")


def load_data(filepath):
    return pd.read_csv(filepath)


def print_value_counts(df):
    # for each column in the data types list
    for column in df.dtypes.index:
        # if the column is of type object (i.e. categorical)
        if df.dtypes[column] == 'object':
            # count the values and print them
            print(df[column].value_counts())
            print("\n\n")


def print_table(df):
    print(tabulate(df, headers="keys" , tablefmt="orgtbl"))


def plot_value_counts(df, column, title='Value Counts Plot'):
    counts = df[column].value_counts()
    ax = sns.barplot(x=counts.index, y=counts.values)
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.title(title)
    plt.show(ax)


def boxplot(df, x, y=None, title='Boxplot'):
    ax = sns.boxplot(x=x, y=y, data=df)
    plt.title(title)
    plt.show(ax)


if __name__ == '__main__':
    # load the data from a CSV file
    data = load_data('data/student-data.csv')
    
    # print the descriptive statistics
    print(data.describe().round(2))
    
    # show a boxplot of 'age' in 2 groups (passed or not)
    boxplot(data, x='age', y='passed', title='Age vs. Passed - Boxplot')
