import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def periods_where_pv_is_null(df_inputs:pd.DataFrame, samples_per_day:int=24):
    """
    Compute the time periods where the PV generation is always 0 for the solar track.
    :param df_inputs: solar track data.
    :return: indices where PV is always 0.
    """
    print(len(df_inputs))
    # Determine time periods where PV generation is 0
    nb_days = int(df_inputs['POWER'].shape[0] / (samples_per_day)) 
    print(nb_days)
    max_power = df_inputs['POWER'].values.reshape(nb_days, samples_per_day).max(axis=0) # reshape to match new intervals
    indices = np.where(max_power == 0)[0]

    print('Indices where PV is always 0:', indices)

    return indices

def load_data(path_name: str, random_state: int = 0, test_size:int=2*12*2, samples_per_day:int=24):
    """
    Build the load power data for the GEFcom IJF_paper case study.
    """
    df_load = pd.read_csv(path_name, parse_dates=True, index_col=0)
    max_load = df_load['POWER'].max()
    indices = periods_where_pv_is_null(df_inputs=df_load, samples_per_day=samples_per_day)

    # Select all columns that are not 'TIMESTAMP' or 'POWER'
    features = [col for col in df_load.columns if col not in ['TIMESTAMP', 'POWER']]

    nb_days = int(len(df_load) / samples_per_day)
    x = np.concatenate([df_load[col].values.reshape(nb_days, samples_per_day) for col in features], axis=1)
    y = df_load['POWER'].values.reshape(nb_days, samples_per_day) / max_load
    y = np.delete(y, indices, axis=1)
    df_y = pd.DataFrame(data=y, index=df_load['POWER'].asfreq('D').index)
    df_x = pd.DataFrame(data=x, index=df_load['POWER'].asfreq('D').index)

    # Decomposition between LS, VS & TEST sets (TRAIN = LS + VS)
    df_x_train, df_x_TEST, df_y_train, df_y_TEST = train_test_split(df_x, df_y, test_size=test_size,
                                                                    random_state=random_state, shuffle=True)
    df_x_LS, df_x_VS, df_y_LS, df_y_VS = train_test_split(df_x_train, df_y_train, test_size=test_size,
                                                          random_state=random_state, shuffle=True)

    nb_days_LS = len(df_y_LS)
    nb_days_VS = len(df_y_VS)
    nb_days_TEST = len(df_y_TEST)
    print('#LS %s days #VS %s days # TEST %s days' % (nb_days_LS, nb_days_VS, nb_days_TEST))

    return df_x_LS, df_y_LS, df_x_VS, df_y_VS, df_x_TEST, df_y_TEST, indices

def dump_file(dir:str, name: str, file):
    """
    Dump a file into a pickle.
    """
    file_name = open(dir + name + '.pickle', 'wb')
    pickle.dump(file, file_name)
    file_name.close()

def read_file(dir:str, name: str):
    """
    Read a file dumped into a pickle.
    """
    file_name = open(dir + name + '.pickle', 'rb')
    file = pickle.load(file_name)
    file_name.close()

    return file

if __name__ == "__main__":
    # Set the working directory to the root of the project
    print(os.getcwd())

    # --------------------------------------------------------------------------------------------------------------
    # NEW DATASET
    # --------------------------------------------------------------------------------------------------------------
    load_data = load_data(path_name='data/load_data_track1.csv', test_size=50, random_state=0)