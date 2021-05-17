import matplotlib.pyplot as plt

def plot_diff(df,col_name1, col_name2):
    plt.plot(df[col_name1], df[col_name2], 'o-')
    plt.title(f'Differences between {col_name2} scores', fontsize=15)
    plt.grid()
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
