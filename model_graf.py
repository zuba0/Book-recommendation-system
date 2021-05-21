import matplotlib.pyplot as plt
from surprise.model_selection import GridSearchCV

def plot_diff(df,col_name1, col_name2):
    plt.plot(df[col_name1], df[col_name2], 'o-')
    plt.title(f'Differences between {col_name2} scores', fontsize=15)
    plt.grid()
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)


def grid_knn(data, model_dict, k, min_k, similarities_list, user_based, cv=5):
    results_list = []
    #Define param grid
    param_grid = dict()
    param_grid['k'] = k
    param_grid['min_k'] = min_k
    param_grid['sim_options'] = dict()
    param_grid['sim_options']['name'] = similarities_list
    param_grid['sim_options']['user_based'] = user_based
    for name, model in model_dict.items():
        grid = GridSearchCV(model,param_grid, cv=cv, n_jobs=-1)
        grid.fit(data)
        print(f' Best parameters for model {name} are {grid.best_params}')
        results_list.append((name, grid))
    return results_list


def find_idx(scoring, model):
    idx_list = []
    params = model.cv_results['params']
    best_sim = model.best_params[scoring]['sim_options']['name']
    for dict_temp in params:
        if dict_temp['sim_options']['name'] == best_sim:
            idx_list.append(params.index(dict_temp))
    return (idx_list, best_sim)


def plot_grid_results(model_name, model, k_list, min_k_list, measure, length, num, scale, sim):
    plt.subplot(length, 2, num)
    plt.title(model_name + ' vs ' + measure + '(' + sim + ')', loc='center', fontsize=15)
    for z in range(scale):
        y = model[z::scale]
        plt.plot(k_list, y, marker='o', label='min_k = ' + str(min_k_list[z]))
    plt.xlabel('k', fontsize=15)
    plt.xticks(fontsize=10, rotation=90)
    plt.yticks(fontsize=10)
    plt.ylabel(measure + 'Value', fontsize=15)
    plt.legend(fontsize=10, loc='best')
    plt.grid()


def hiper_visual(models_info, min_k_list, k_list):
    plt.figure(figsize=(25, 25))

    scale = len(min_k_list)
    j = 0
    for i in range(len(models_info)):
        j += 1
        #Read the model
        model = models_info[i][1]
        #Find which similarity type achieve the lowest scores and find indexes of params with this similarity
        rmse_idx_list, rmse_best_sim = find_idx('rmse', model)
        mae_idx_list, mae_best_sim = find_idx('mae', model)
        #Take only params from list above
        model_rmse = model.cv_results['mean_test_rmse'][rmse_idx_list]
        model_mae = model.cv_results['mean_test_mae'][mae_idx_list]

        plot_grid_results(model_name=models_info[i][0], model=model_rmse, k_list=k_list, min_k_list=min_k_list,
                          measure='RMSE', length=len(models_info), num=j, scale=scale, sim=rmse_best_sim)

        j += 1

        plot_grid_results(model_name=models_info[i][0], model=model_mae, k_list=k_list, min_k_list=min_k_list,
                          measure='MAE', length=len(models_info), num=j, scale=scale, sim=mae_best_sim)




    plt.show()




