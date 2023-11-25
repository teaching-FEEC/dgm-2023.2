import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('Resultados/Treinamento-Unicamp/unicamp-database-fixed.csv')

# Step 2: Normalize the 'POWER' column
df['POWER'] = df['POWER'] / df['POWER'].max()

# Step 3: Save the normalized dataframe to a new CSV file
df.to_csv('Resultados/Treinamento-Unicamp/unicamp-database-fixed-normalized.csv', index=False)