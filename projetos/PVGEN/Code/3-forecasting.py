import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sklearn.preprocessing
import optuna
import numpy as np
import random
import tensorflow as tf
from tensorflow import keras
from keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, InputLayer
from optuna.visualization import plot_optimization_history, plot_parallel_coordinate, plot_contour, plot_param_importances
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.models import load_model
import sklearn.metrics as metrics
import tensorflow as tf
import keras

## CONFIG 1 ##
path_df = 'data_pv/gecad_from-unicamp-holanda.csv' # 'data/gecad_from-unicamp-holanda/'
path_sets= 'sets_pv/gecad_from-unicamp-holanda/' # 'sets/gecad_from-unicamp-holanda/'
time_interval  = 60
days_backs = 3
type_jump = 'daily'
horizont  = 15 
fcst_feature = 'power' 

## CONFIG 2 ##
path_models = 'models_pv/'
horizont  = 15
days_backs = 3
epochs = 30
n_trials = 5
exp = 2 
storage= f"sqlite:///LSTM_study_{exp}.db"
study_name=f"LSTM_study_{exp}"
path_model_check = f"{path_models}/check_model_h{horizont}_s{exp}.h5"
path_model_best = f"{path_models}/best_model_h{horizont}_s{exp}.h5"
path_df_study = f'{path_models}/df_h{horizont}_e{exp}.csv'

###############################################################
##                    CREATE DATASETS                        ##
###############################################################

## FUNCTIONS
def normalize_data(df):
    min_max_scaler = sklearn.preprocessing.MinMaxScaler()
    variables = list(df.columns)
    for norm_variable in variables:
        df[norm_variable] = min_max_scaler.fit_transform(df[norm_variable].values.reshape(-1,1))
    return df

## MAIN
df_input = pd.read_csv(path_df, index_col=0 , parse_dates=['datetime'])
df_input= df_input.between_time('06:00:00', '20:00:00')
features = ['power', 'AirTemp', 'RelativeHumidity','Ghi', 'WindSpeed10m',  'Zenith']
df_input = df_input[features]

first_train_day = df_input.index[0]
first_val_day = datetime(2020, 8, 9)
first_test_day = datetime(2021, 4, 19)
last_test_date = df_input.index[-1]
aux_info = df_input[df_input.index.date == df_input.index[0].date()]
aux_hour = aux_info.index[-1]
aux_hour2 = df_input[df_input.index.date > df_input.index[0].date()].index[0]
aux_dif_hours = aux_hour2 - aux_hour
daily_timestep = len(aux_info)
seq_len = days_backs*daily_timestep
max_hour = aux_info.index[-1].time()
aux_fcst_date = first_train_day + timedelta(days=days_backs)

df = normalize_data(df_input.copy())
df = df.dropna()
x_train,y_train,x_valid = [], [], []
y_valid, x_test, y_test = [], [], []

datas_fsct = []
while aux_fcst_date.date() <= last_test_date.date():
  aux_daybacks = aux_fcst_date - timedelta(days=days_backs)
  aux_input = df[(df.index >= aux_daybacks)&(df.index < aux_fcst_date)]
  aux_df_output = df[(df.index >= aux_fcst_date)&(df.index < (aux_fcst_date+timedelta(days=2)))]
  aux_df_output = aux_df_output.iloc[0:horizont]
  if len(aux_input)+len(aux_df_output) == seq_len+horizont:
    if aux_fcst_date < first_val_day:
      x_train.append(aux_input.values.T)
      y_train.append(aux_df_output[fcst_feature].values.T)
    elif aux_fcst_date < first_test_day:
      x_valid.append(aux_input.values.T)
      y_valid.append(aux_df_output[fcst_feature].values.T)  
    elif aux_fcst_date >= first_test_day:
      x_test.append(aux_input.values.T)
      y_test.append(aux_df_output[fcst_feature].values.T)

  if type_jump == 'daily':
    datas_fsct.append(aux_fcst_date.date())
    aux_fcst_date = aux_fcst_date + timedelta(days=1)
  else:
    if aux_fcst_date.time() == max_hour :
      aux_fcst_date = aux_fcst_date+ aux_dif_hours
    else:
      aux_fcst_date = aux_fcst_date+timedelta(minutes=time_interval)

x_train ,y_train = np.array(x_train), np.array(y_train)
x_valid, y_valid = np.array(x_valid), np.array(y_valid)
x_test, y_test  = np.array(x_test), np.array(y_test)

np.save(f'{path_sets}x_train_{days_backs}_h{horizont}.npy',x_train)
np.save(f'{path_sets}y_train_{days_backs}_h{horizont}.npy',y_train)
np.save(f'{path_sets}x_valid_{days_backs}_h{horizont}.npy',x_valid)
np.save(f'{path_sets}y_valid_{days_backs}_h{horizont}.npy',y_valid)
np.save(f'{path_sets}x_test_{days_backs}_h{horizont}.npy',x_test)
np.save(f'{path_sets}y_test_{days_backs}_h{horizont}.npy',y_test)


###############################################################
##                    HPO with OPTUNA                        ##
###############################################################

## SEEDS
np.random.seed(42)
tf.random.set_seed(42)
random.seed(42)

def create_model(trial):
    # Define the hyperparameters to optimize
    units = [trial.suggest_int(f"units_{i}", 32, 128) for i in range(1, 5)]
    units_FC = trial.suggest_int("dense_units", 32, 128)
    dropout_rate = trial.suggest_float("dropout_rate", 0.0, 0.5, step=0.05)
    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-3, log=True)
    num_layers = trial.suggest_int("num_layers", 1, 4)
    tf.keras.backend.clear_session()
    np.random.seed(42)
    tf.random.set_seed(42)
    random.seed(42)
    # Create the LSTM model
    model = Sequential()
    model.add(InputLayer(input_shape=(x_train.shape[1],x_train.shape[2])))
    # Add LSTM layers
    if num_layers ==1:
        model.add(LSTM(units[0], return_sequences=False))
    else:
        for i in range(num_layers):
            if i == num_layers - 1:
                model.add(LSTM(units[i], return_sequences=False))
            else:
                model.add(LSTM(units[i], return_sequences=True))
    model.add(Dropout(dropout_rate))
    # Add Dense layer
    model.add(Dense(units=units_FC))
    # Output layer
    model.add(Dense(y_train.shape[1]))
    model.compile(loss='mse', optimizer=keras.optimizers.Adam(learning_rate=learning_rate))
    return model

def objective(trial):
    model = create_model(trial)
    checkpoint = ModelCheckpoint(path_model_check, save_best_only=True, monitor='val_loss', mode='min')
    es = EarlyStopping(
    monitor="val_loss",  
    patience=5,  
    verbose=1,
    mode="auto", 
    restore_best_weights=True,
    )
    # Train the model with the hyperparameters suggested by Optuna
    model.fit(x_train, y_train, validation_data=(x_valid, y_valid), epochs=epochs, batch_size=64, verbose=0, callbacks=[es,checkpoint])
    # Load the best model
    best_model = load_model(path_model_check) 
    # Evaluate the best model on the validation set
    loss = best_model.evaluate(x_valid, y_valid, verbose=1)
    # Save weights
    if trial.number == 0:  # first trial
        best_model.save(path_model_best)
    else:
        if loss < study.best_trial.value:  # if current trial is better
            best_model.save(path_model_best)
    return loss


study = optuna.create_study(study_name=study_name, storage=storage, direction="minimize")
study.optimize(objective, n_trials=n_trials)

# Print the best results
best_trial = study.best_trial
print("Lowest loss value: {}".format(best_trial.value))
print("Best hyperparameters: ")
for key, value in best_trial.params.items():
    print("{}: {}".format(key, value))