import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error

def plot_prediction(y_true: np.array, y_pred: np.array, save_path: str=None):
    r2 = r2_score(y_true, y_pred)
    # text annotation setup
    plt.title(r"True values vs predicted values ($R^2$ = " + f'{r2:.4f}' + ')')
    plt.xlabel("True values")
    plt.ylabel("Predicted values")
    # plot the scatter and line
    plt.scatter(y_true, y_pred, c='red', marker='o')
    plt.plot(y_true, y_true, 'b--')
    # show the plot!
    plt.savefig(save_path if save_path else 'pred.png')

def train_model(X_train, y_true_train) -> object:
    model = LinearRegression()
    model.fit(X_train, y_true_train)
    return model

def evaluate_model(model: LinearRegression, X, y_true, mode: str, save_path: str=None):
    y_pred = model.predict(X)
    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    print(f"{mode} R^2: {r2:.4f}")
    print(f"{mode} RMSE: {rmse:.4f}")
    plot_prediction(y_true, y_pred, save_path=save_path)
    return rmse, r2