import pandas as pd

# Read the CSV file
df = pd.read_csv('Resultados/Treinamento-Unicamp2unicamp/unicamp-database-fixed.csv')

# Convert 'TIMESTAMP' to datetime format
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

# Create a new dataframe that only contains data from 2023
df_2023 = df[df['TIMESTAMP'].dt.year == 2023]

# Create another dataframe that contains data from other years
df_other_years = df[df['TIMESTAMP'].dt.year != 2023]

# Write 'df_2023' to a new CSV file
df_2023.to_csv('unicamp2023.csv', index=False)

# Write 'df_other_years' to a new CSV file
df_other_years.to_csv('unicamp2019_2022.csv', index=False)