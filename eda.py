def show_df_info(df):
    print('Head : ')
    display(df.head())
    print(f'Number of rows : {len(df)}')
    print('Number of NaN values in each column : ')
    display(df.isna().sum())

def show_duplicates(df):
    print('Number of duplicated rows : ')
    display(df.duplicated().sum())
