"""This module contains functions used for Exploatory Data Analysis."""

import random
import dexplot

def rows_number(df):
    """
    Show number of rows in DataFrame.
    :param df: Pandas DataFrame.
    """
    print(f'Number of rows is {len(df)}')

def unique_values(df):
    """
    Show number of unique values for each column in DataFrame.
    :param df: Pandas DataFrame.
    """
    for col in df.columns:
        print(f' Number of unique values in {col} column is {len(df[col].unique())}')

def grouping(df, col_name):
    """
    Show number of unique values for each column in DataFrame.
    :param df:        Pandas DataFrame.
    :param col_name:  Name of column.
    :return DataFrame grouped by given column with count aggregation function
    """

    return df.groupby(col_name)['rating'].count()

def show_df_info(df):
    """
    Show basic information about DataFrame : header,
    number of rows, number of NaNs and unique values in each column.
    :param df: Pandas DataFrame.
    """
    print('Header : ')
    display(df.head())
    rows_number(df)
    print('Number of NaN values in each column : ')
    display(df.isna().sum())
    unique_values(df)

def show_duplicates(df):
    """
    Show number of duplicated rows in given DataFrame
    :param df: Pandas DataFrame.
    """
    print('Number of duplicated rows : ')
    display(df.duplicated().sum())

def choose_values(n, df, col_name):
    """
    Show number of duplicated rows in given DataFrame
    :param df: Pandas DataFrame.
    """
    # list of unique values in column col_name
    val_list = list(df[col_name].unique())
    # randomly choose n*len(val_list) values from list
    chosen_val = random.sample(val_list, int(n*len(val_list)))
    #
    return df[df[col_name].isin(chosen_val)]



def check_ratings(data, col_name):
    """
    Generate a visualtization
    :param df: Pandas DataFrame.
    """
    data_grouped = grouping(data, col_name)
    title = 'Number of ratings per '+ str(col_name[:-3])
    display(dexplot.hist(val='rating',data=data_grouped, title=title, cmap='plasma'))
    print('Statistics for dataframe grouped by '+ str(col_name) +':')
    print(data_grouped.describe())

