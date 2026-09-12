from data_extraction import dataframe_formation
import pandas as pd
import numpy as np

file1 = 'internet_costs_2025.txt'
file2 = 'internet_speeds_2026.txt'

costdf, speeddf = dataframe_formation(file1, file2)
dataframe3 = {'country': [], 'cost': [], 'speed': []}

for index, row in costdf.iterrows():
    country = row['country']
    row2 = speeddf.loc[speeddf['country'] == country]

    if not row2.empty:
        speed = float(row2['mobile connectivity(download)'].iloc[0]) if row2['mobile connectivity(download)'].iloc[0] != '' else np.nan
        cost = float(row['broadband cost adj'][1:]) if row['broadband cost adj'][1:] != '' else np.nan
        dataframe3['country'].append(country)
        dataframe3['cost'].append(cost)
        dataframe3['speed'].append(speed)

corr_df = pd.DataFrame(dataframe3)
clean = corr_df[['cost', 'speed']].dropna()

cost = clean['cost']
speed = clean['speed']

corr = np.corrcoef(cost, speed)[0, 1]
print(corr)
