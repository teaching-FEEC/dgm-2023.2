
from GEFcom2014.models import scale_data_gen
from GEFcom2014.utils import load_data_gen
from torch.utils.benchmark import timer
from GEFcom2014.utils import read_file
import pandas as pd
import numpy as np
import torch
import json

# Weather data and generated model
DF_NAME = 'data/Treinamento-Unicamp/df_gecad_to_generate.csv'
model_dir = "data/Treinamento-Unicamp/export/multi_nfs/"
model_name = "model_AN_M_1_0_best"
config = json.load(open(f"{model_dir}/AN_M_1.json", "r"))

#UNICAMP-HOLANDA
# DF_NAME = 'data/Treinamento-Unicamp_holanda/gecad_modified_ordered.csv'
# model_dir = "data/Treinamento-Unicamp_holanda/export/multi_nfs/"
# model_name = "model_UMNN_M_1_0_best"
# config = json.load(open(f"{model_dir}/UMNN_M_1.json", "r"))

#UNICAMP TO UNICAMP
# DF_NAME = 'data/Treinamento-Unicamp2unicamp/unicamp2023.csv'
# model_dir = "data/Treinamento-Unicamp2unicamp/export/multi_nfs/"
# model_name = "model_AN_M_1_0_best"
# config = json.load(open(f"{model_dir}/AN_M_1.json", "r"))


# load flow model from file:
best_flow = read_file(dir=model_dir, name=model_name)
# config = json.load(open("{model_dir}/UMNN_M_1.json", "r"))

df_real = pd.read_csv(DF_NAME, index_col='TIMESTAMP', parse_dates=True)

dataset_dir = DF_NAME
data = load_data_gen(path_name=dataset_dir, samples_per_day=24)

df_x = data[0]
df_y = data[1]
indices = data[2]

x_scaled, y_scaled, y_scaler = scale_data_gen(x=df_x.values, y=df_y.values)

non_null_indexes = list(np.delete(np.asarray([i for i in range(24)]), indices))

# Rebuilt the PV observations with the removed time periods
df_y.columns = non_null_indexes
for i in indices:
    df_y[i] = 0
df_y = df_y.sort_index(axis=1)



n_s = 100
x = x_scaled
y = y_scaled
flow = best_flow
conditioner_args = config['conditioner_args']
max = 1
gpu = True
#non_null_indexes
samples_per_day  =24



"""
Build scenarios for a NFs multi-output.
Scenarios are generated into an array (n_periods, n_s) where n_periods = 24 * n_days
:return: scenarios (n_periods, n_s)
"""
# to assign the data to GPU with .to(device) on the data
if gpu:
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
else:
    device = "cpu"
flow.to(device)

n_periods_before = non_null_indexes[0]
n_periods_after = samples_per_day - non_null_indexes[-1] - 1
print(n_periods_after, n_periods_before)

n_days = len(x)
nb_output, cond_in = conditioner_args['in_size'], conditioner_args['cond_in']
time_tot = 0.
scenarios = []
for i in range(n_days):
    start = timer()
    # sample nb_scenarios per day
    # predictions = flow.invert(z=torch.randn(n_s, nb_output).to(device), context=torch.tensor(np.tile(x[i, :], n_s).reshape(n_s, cond_in)).to(device).float()).cpu().detach().numpy()
    # Assuming the correct shape is (10, 216)
    predictions = flow.invert(z=torch.randn(n_s, nb_output).to(device), context=torch.tensor(np.tile(x[i, :], n_s).reshape(n_s, cond_in)).to(device).float()).cpu().detach().numpy()

    # predictions = flow.invert(z=torch.randn(n_s, nb_output).to(device), context=torch.tensor(np.tile(x[i, :], n_s).reshape(n_s, 216)).to(device).float()).cpu().detach().numpy()
    predictions = y_scaler.inverse_transform(predictions)

    # corrections -> genereration is always > 0 and < max capacity
    predictions[predictions < 0] = 0
    predictions[predictions > max] = max
    # fill time period where PV is not 0 are given by non_null_indexes
    # for instance it could be [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # then it is needed to add 0 for periods [0, 1, 2, 3] and [20, 21, 22, 23]

    scenarios_tmp = np.concatenate((np.zeros((predictions.shape[0], n_periods_before)), predictions, np.zeros((predictions.shape[0], n_periods_after))), axis=1)  # shape = (n_s, 24)
    scenarios.append(scenarios_tmp.transpose()) # list of arrays of shape (24, n_s)
    end = timer()
    time_tot += end - start
    print("day {:.0f} Approximate time left : {:2f} min".format(i, time_tot / (i + 1) * (n_days - (i + 1))/60), end="\r",flush=True)
    # if i % 20 == 0:
    #     print("day {:.0f} Approximate time left : {:2f} min".format(i, time_tot / (i + 1) * (nb_days - (i + 1)) / 60))
print('Scenario generation time_tot %.1f min' % (time_tot / 60))
returned = np.concatenate(scenarios,axis=0) # shape = (24*n_days, n_s)

# Calculate the average prediction for each hour
Pmax = df_real.POWER.max()
average_prediction = np.mean(returned, axis=1)
real_normalized = df_real.POWER.values / df_real.POWER.max()


import matplotlib.pyplot as plt

def plot_day(day, real, prediction):
    plt.figure()
    plt.plot(real[(day-1)*24:day*24], label = 'real')
    plt.plot(prediction[(day-1)*24:day*24], label = 'gerado')
    plt.legend()
    plt.tight_layout()
    plt.show()
    return


N = 10  # replace with the day number you're interested in
from sklearn.metrics import mean_absolute_error
import numpy as np

# Remove NaN values from real_normalized
real_normalized = real_normalized[~np.isnan(real_normalized)]

# Calculate the average prediction for each hour
Pmax = df_real.POWER.max()
real_normalized = df_real.copy()
real_normalized['POWER'] = real_normalized['POWER']

# Force zero values between 21h and 5h
predictions = df_real.copy()
predictions['POWER'] = average_prediction
predictions.loc[predictions.index.hour < 6, 'POWER'] = 0
predictions.loc[predictions.index.hour > 20, 'POWER'] = 0


mae = mean_absolute_error(
    real_normalized.POWER.between_time('06:00:00', '20:00:00'), 
    predictions.POWER.between_time('06:00:00', '20:00:00')
)
rmse = np.sqrt(np.mean((real_normalized.POWER - predictions.POWER) ** 2))

print(f'MAE: {mae}')
print(f'RMSE: {rmse}')


predictions.to_csv('gecad_from-unicamp.csv')
print('fim do programa')



def plot_days_vector(start, end, real, prediction):
    plt.figure()
    plt.plot(real[(start-1)*24:end*24], label=f'Real')
    plt.plot(prediction[(start-1)*24:end*24], label=f'Fake')
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('Power (W)')
    plt.tight_layout()
    plt.savefig(f'gerado.svg')
    plt.show()

# Usage example
plot_days_vector(1,30, df_real.POWER/Pmax, predictions.POWER)