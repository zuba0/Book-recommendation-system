"""This module contains functions used for algorithms results visualization"""

import matplotlib.pyplot as plt


def find_idx(scoring, model):
    """
    Finds for which similarity measure the model achieve the best scoring.
    Looks for tested sets of parameters which contains this similarity measure.
    Returns list of indexes of these sets and name of similarity measure from best model.
    :param scoring:       Scoring type used in model evaluation
    :param model:         Predefined model
    :return               Tuple with list of index and similarity measure name from best model
    """
    idx_list = []
    params = model.cv_results['params']
    best_sim = model.best_params[scoring]['sim_options']['name']
    for dict_temp in params:
        if dict_temp['sim_options']['name'] == best_sim:
            idx_list.append(params.index(dict_temp))
    return idx_list, best_sim


def plot_grid_results(model_name, model, k_list, min_k_list, measure, row_num, num, sim):
    """
    Plots a dependency chosen scoring on parameters k and min_k
    :param model_name:      Model's name
    :param model:           Predefined model
    :param k_list:          List of k parameters
    :param min_k_list:      List of min_k parameters
    :param measure:         Used measure
    :param row_num:         Row number
    :param num:             Plot number
    :param sim:             Name of used similarity measure
    """
    plt.subplot(row_num, 2, num)
    plt.title(model_name + ' vs ' + measure + ' (' + sim + ')', loc='center', fontsize=15)
    scale = len(min_k_list)
    # Plots a line for each min_k parameter
    for z in range(scale):
        y = model[z::scale]
        plt.plot(k_list, y, marker='o', label='min_k = ' + str(min_k_list[z]))
    plt.xlabel('k', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel(measure + 'Value', fontsize=20)
    plt.legend(fontsize=15, loc='best')
    plt.grid()


def plot_scoring_results(models_info, k_list, min_k_list):
    """
    Plots two charts : one for RMSE scoring and one for MAE scoring.
    Each one shows dependency of scoring on models parameters.
    :param models_info:     List of tuples with models and their names
    :param k_list:          List of k parameters
    :param min_k_list:      List of min_k parameters
    """
    plt.figure(figsize=(30, 30))
    j = 0
    for i in range(len(models_info)):
        j += 1
        # Read the model
        model = models_info[i][1]
        # Find which similarity type achieve the best scores and find indexes of params with this similarity
        rmse_idx_list, rmse_best_sim = find_idx('rmse', model)
        mae_idx_list, mae_best_sim = find_idx('mae', model)
        # Take only params from list above
        model_rmse = model.cv_results['mean_test_rmse'][rmse_idx_list]
        model_mae = model.cv_results['mean_test_mae'][mae_idx_list]

        plot_grid_results(model_name=models_info[i][0], model=model_rmse, k_list=k_list, min_k_list=min_k_list,
                          measure='RMSE', row_num=len(models_info), num=j, sim=rmse_best_sim)

        j += 1

        plot_grid_results(model_name=models_info[i][0], model=model_mae, k_list=k_list, min_k_list=min_k_list,
                          measure='MAE', row_num=len(models_info), num=j, sim=mae_best_sim)

    plt.show()


def plot_diff(df, models, scoring):
    """
    Visualize how the values of chosen scoring change for different models
    :param df:            Pandas DataFrame
    :param models:        Name of df column which contains models' names
    :param scoring:       Type of scoring
    """
    plt.plot(df[models], df[scoring], 'o-')
    plt.title(f'Differences between {scoring} scores', fontsize=15)
    plt.grid()
    plt.xticks(fontsize=15, rotation=90)
    plt.yticks(fontsize=15)
