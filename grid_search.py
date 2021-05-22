"""This module contains grid searches for knn and matrix factorization algorithms"""

from surprise.model_selection import GridSearchCV


def perform_grid_search(data, model_dict, param_grid, cv):
    """
    Return list of trained models in GridSearch
    :param data:               Trainset to use in model training
    :param model_dict:         Dictionary with list of models(and their names) to be used
    :param param_grid:         Dictionary with algorithm parameters
    :param cv:                 Determines the cross-validation splitting. By default 5-fold.
    :return                    List of trained models
    """
    results_list = []
    for name, model in model_dict.items():
        grid = GridSearchCV(model, param_grid, cv=cv, n_jobs=-1)
        grid.fit(data)
        print(f'Best parameters for model {name} are {grid.best_params}')
        results_list.append((name, grid))
    return results_list


def grid_knn(data, model_dict, k_list, min_k_list, similarities_list, user_based, cv=5):
    """
    Return list of trained models in GridSearch for KNN algorithms
    :param data:               Trainset to use in model training
    :param model_dict:         Dictionary with list of models(and their names) to be used
    :param k_list:             List of k values
    :param min_k_list:         List of min_k values
    :param similarities_list:  List of similarity measures
    :param user_based:         Defines user-based or item-based approach
    :param cv:                 Determines the cross-validation splitting. By default 5-fold.
    :return                    List of trained models
    """
    # Define param grid
    param_grid = dict()
    param_grid['k'] = k_list
    param_grid['min_k'] = min_k_list
    param_grid['sim_options'] = dict()
    param_grid['sim_options']['name'] = similarities_list
    param_grid['sim_options']['user_based'] = [user_based]
    results = perform_grid_search(data, model_dict, param_grid, cv)
    return results


def grid_matrix_fact(data, model_dict, n_epochs, n_factors, lr_all, reg_all, cv=5):
    """
    Return list of trained models in GridSearch for SVD algorithm
    :param data:               Trainset to use in model training
    :param model_dict:         Dictionary with list of models(and their names) to be used
    :param n_epochs:           List of n_epochs values
    :param n_factors:          List of n_factors values
    :param lr_all:             List of lr_all values
    :param reg_all:            List of reg_all values
    :param cv:                 Determines the cross-validation splitting. By default 5-fold.
    :return                    List of trained models
    """
    # Define param grid
    param_grid = dict()
    param_grid['n_epochs'] = n_epochs
    param_grid['lr_all'] = lr_all
    param_grid['n_factors'] = n_factors
    param_grid['reg_all'] = reg_all
    results = perform_grid_search(data, model_dict, param_grid, cv)
    return results
