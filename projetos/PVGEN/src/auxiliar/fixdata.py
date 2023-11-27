import pandas as pd

# Step 2
df = pd.read_csv('Resultados/Treinamento-Unicamp_holanda/training_database.csv')

# Step 3
df = df.dropna()

# Step 4 and 5
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df = df.set_index('TIMESTAMP')

# Step 6 and 7
df = df.resample('1H').ffill()

# Step 8
df = df[df.groupby(df.index.date).transform('count').eq(24)]

# Step 9
df = df.reset_index()

# step 10 save
df.to_csv('teste.csv', index=False)
