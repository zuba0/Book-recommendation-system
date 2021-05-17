import random
import dexplot

def show_df_info(df):
    print('Header : ')
    display(df.head())
    print(f'Number of rows : {len(df)}')
    print('Number of NaN values in each column : ')
    display(df.isna().sum())

def show_duplicates(df):
    print('Number of duplicated rows : ')
    display(df.duplicated().sum())

def choose_values(n, df, col_name):
    val_list = list(df[col_name].unique())
    chosen_val = random.sample(val_list, int(n*len(val_list)))
    return df[df[col_name].isin(chosen_val)]

def grouping(data, col_name):

    return data.groupby(col_name)['rating'].count()

def check_ratings(data, col_name):
    data_grouped = grouping(data, col_name)
    title = 'Number of ratings per '+ str(col_name[:-3])
    display(dexplot.hist(val='rating',data=data_grouped, title=title, cmap='plasma'))
    print('Statistics for dataframe grouped by '+ str(col_name) +':')
    print(data_grouped.describe())