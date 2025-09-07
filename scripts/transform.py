import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
df.to_csv('data_clean.csv', index=False)