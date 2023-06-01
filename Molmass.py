import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(io='/Users/ageldinov/Documents/PSGtest/PKTESTDATA.xlsx')

print(df)

start_time = df['Time'][0]
end_time = df['Time'][len(df)-1]

start_conc = df['Conc'][0]
end_conc = df['Conc'][len(df)-1]

half_life = 0.5 * (start_conc/end_conc)

half_life = round(half_life, 3)

print(half_life)

max_conc = max(df['Conc'])

for i in range(len(df)):
    if max_conc == df['Conc'][i]:
        max_time = df['Time'][i]

print(max_time, max_conc)

graph = df.plot(x='Time', y='Conc', kind='line')

elimination_rate = ((np.log(df['Conc'][0])) - np.log((df['Conc'][len(df)-1]))) / (df['Time'][0] - df['Time'][len(df) - 1])

print(elimination_rate)
