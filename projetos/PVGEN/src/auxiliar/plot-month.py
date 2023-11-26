import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df_fake = pd.read_csv('new-data/gecad_generated_from_unicamp.csv')
df_real = pd.read_csv('gecad_modified_ordered.csv')

# Convert 'TIMESTAMP' to datetime format
df_fake['TIMESTAMP'] = pd.to_datetime(df_fake['TIMESTAMP'])
df_real['TIMESTAMP'] = pd.to_datetime(df_real['TIMESTAMP'])

def plot_power(days):
    # Filter dataframe to include only the specified number of days
    df_days_fake = df_fake[df_fake['TIMESTAMP'] < df_fake['TIMESTAMP'][0] + pd.Timedelta(days=days)]
    df_days_real = df_real[df_real['TIMESTAMP'] < df_real['TIMESTAMP'][0] + pd.Timedelta(days=days)]

    # Plot 'POWER'
    plt.figure(figsize=(10,6))
    plt.plot(df_days_fake['TIMESTAMP'], df_days_fake['POWER'], label='Fake')
    plt.plot(df_days_real['TIMESTAMP'], df_days_real['POWER'], label='Real')
    plt.xlabel('Timestamp')
    plt.ylabel('Power')
    plt.title(f'Power over {days} day(s)')
    plt.legend()
    plt.show()

# Example usage: 
plot_power(30)