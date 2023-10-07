import pandas as pd

df = pd.read_csv('Que3.csv')

df['Temperature'] = (df['Temperature'] * 9/5) + 32

max_temp_table = df.groupby(['Zone', 'Date']).agg({'Temperature': 'max', 'ReportType': lambda x: ', '.join(x.unique())}).reset_index()

avg_temp_table = df.groupby('Zone')['Temperature'].mean().reset_index()

print("Max Temperature by Zone, Date, and Combined Report Type:")
print(max_temp_table)

print("\nAverage Temperature by Zone:")
print(avg_temp_table)
