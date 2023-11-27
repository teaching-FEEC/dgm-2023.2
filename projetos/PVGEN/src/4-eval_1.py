import numpy as np
import pandas as pd
from keras.models import load_model
import sklearn.metrics as metrics
import tensorflow as tf
import keras
import random

## SEEDS
np.random.seed(42)
tf.random.set_seed(42)
random.seed(42)

path_sets = f'sets_pv/gecad_from-unicamp/' #gecad_from-unicamp or gecad_from-unicamp-holanda
path_models = f'models_pv' #PRE-TRAINED MODEL
horizont  = 15
days_backs = 3
exp = 1 #
path_model_best = f"{path_models}/best_model_h{horizont}_s{exp}.h5"

###############################################################

# Load the training, validation, and test datasets
x_train = np.load(f'{path_sets}x_train_{days_backs}_h{horizont}.npy')
y_train = np.load(f'{path_sets}y_train_{days_backs}_h{horizont}.npy')
x_valid = np.load(f'{path_sets}x_valid_{days_backs}_h{horizont}.npy')
y_valid = np.load(f'{path_sets}y_valid_{days_backs}_h{horizont}.npy')
x_test = np.load(f'{path_sets}x_test_{days_backs}_h{horizont}.npy')
y_test = np.load(f'{path_sets}y_test_{days_backs}_h{horizont}.npy')
y_valid = y_valid.reshape(y_valid.shape[0],y_valid.shape[1])
y_test = y_test.reshape(y_test.shape[0],y_test.shape[1])

model = keras.models.load_model(path_model_best)
print(model.summary())

## Val
y_pred_val = model.predict(x_valid, verbose=0)
mae_val = metrics.mean_absolute_error(y_valid, y_pred_val)
rmse_val = np.sqrt(metrics.mean_squared_error(y_valid, y_pred_val))

y_pred_test = model.predict(x_test, verbose=0)
mae_test = metrics.mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))


print(f'**** Performance of best model ****\n')
print('metric |  valid  |  test   |')
print('----------------------------')
print(f' MAE   | {mae_val:.5f} | {mae_test:.5f} |')
print(f' RMSE  | {rmse_val:.5f} | {rmse_test:.5f} |')