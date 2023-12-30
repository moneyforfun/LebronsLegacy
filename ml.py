import pandas as pd
s = pd.read_csv('player_mvp_stats.csv')
del s['Unnamed: 0']
s = s.fillna(0)
print(s.columns)