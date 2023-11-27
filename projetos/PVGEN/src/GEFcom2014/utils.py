import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')

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
    df_load = df_load.dropna()
    max_load = df_load['POWER'].max()
    indices = periods_where_pv_is_null(df_inputs=df_load, samples_per_day=samples_per_day)
    # Select all columns that are not 'TIMESTAMP' or 'POWER'
    features = [col for col in df_load.columns if col not in ['TIMESTAMP', 'POWER']]

    if not isinstance(df_load.index, pd.DatetimeIndex):
        df_load.index = pd.to_datetime(df_load.index, utc=True)

    # Remove timezone information
    df_load.index = df_load.index.tz_localize(None)

    df_load = df_load[df_load.index.minute == 0]

    # Group the data by day
    grouped = df_load.groupby(df_load.index.date)

    # Create a new DataFrame to store the resampled data
    df_resampled = pd.DataFrame()

    # Iterate over each group (day)
    for _, group in grouped:
        # Check if the first timestamp of the day is not at 0:00
        if group.index.min().hour != 0:
            # Create a new date range that starts at 0:00 of the day
            date_range = pd.date_range(start=group.index.min().replace(hour=0), end=group.index.min().replace(hour=23), freq='H')
        else:
            # Create a date range for the day that spans 24 hours
            date_range = pd.date_range(start=group.index.min(), end=group.index.min() + pd.Timedelta(hours=23), freq='H')

        # Reindex the group with the date range and fill missing values with 0
        group = group.reindex(date_range).fillna(0)
        # Append the group to the new DataFrame
        df_resampled = df_resampled.append(group)

    # Group the resampled data by day
    grouped = df_resampled.groupby(df_resampled.index.date)

    # Reshape each group into a 1D array and store it in a list
    x = [group[features].values.flatten() for _, group in grouped if len(group) == samples_per_day]
    y = [group['POWER'].values.flatten() / max_load for _, group in grouped if len(group) == samples_per_day]

    # Convert the lists to numpy arrays
    x = np.array(x)
    y = np.array(y)

    print("First day:")
    print(df_resampled.head(24))
    
    # Remove the indices where PV is always 0
    y = np.delete(y, indices, axis=1)

    # Create pandas DataFrames
    df_y = pd.DataFrame(data=y)
    df_x = pd.DataFrame(data=x)

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

def load_data_gen(path_name: str, samples_per_day:int=24):
    """
    Build the load power data for the GEFcom IJF_paper case study.
    """
    df_load = pd.read_csv(path_name, parse_dates=True, index_col=0)
    df_load = df_load.dropna()
    max_load = df_load['POWER'].max()
    indices = periods_where_pv_is_null(df_inputs=df_load, samples_per_day=samples_per_day)
    # Select all columns that are not 'TIMESTAMP' or 'POWER'
    features = [col for col in df_load.columns if col not in ['TIMESTAMP', 'POWER']]

    # Group the data by day
    grouped = df_load.groupby(df_load.index.date)

    # Reshape each group into a 1D array and store it in a list
    x = [group[features].values.flatten() for _, group in grouped if len(group) == samples_per_day]
    y = [group['POWER'].values.flatten() / max_load for _, group in grouped if len(group) == samples_per_day]

    # Convert the lists to numpy arrays
    x = np.array(x)
    y = np.array(y)

    # Remove the indices where PV is always 0
    y = np.delete(y, indices, axis=1)

    # Create pandas DataFrames
    df_y = pd.DataFrame(data=y)
    df_x = pd.DataFrame(data=x)

    return df_x, df_y, indices

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