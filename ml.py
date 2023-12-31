import pandas as pd
s = pd.read_csv('player_mvp_stats.csv')
del s['Unnamed: 0']
s = s.fillna(0)
print(s.columns)

predictors = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year',
        'W', 'L', 'W/L%', 'GB', 'PS/G',
       'PA/G', 'SRS']

train = s[s['Year'] < 2020]
test = s[s['Year'] == 2020]

from sklearn.linear_model import Ridge
reg = Ridge(alpha=.1)
reg.fit(train[predictors],train['Share'])
predictions = reg.predict(test[predictors])
predictions = pd.DataFrame(predictions, columns=['predictions'], index = test.index)

combination = pd.concat([test[['Player','Share']], predictions],axis=1)
print(combination.sort_values('Share',ascending=False).head(10))

from sklearn.metrics import mean_squared_error

x = mean_squared_error(combination['Share'],combination['predictions'])
print(x)