from bs4 import BeautifulSoup
import requests
import pandas as pd

years = list(range(1991, 2021))
url_start = 'https://www.basketball-reference.com/awards/awards_{}.html'

'''for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open('mvp/{}.html'.format(year),'w+', encoding="utf-8") as f:
        f.write(data.text)'''
'''dfs = []
for year in years:
    with open('mvp/{}.html'.format(year), encoding="utf-8") as f:
        page=f.read( )
    soup = BeautifulSoup(page,'html.parser')
    soup.find('tr', class_='over_header').decompose()
    mvp_table = soup.find(id='mvp')
    mvp = pd.read_html(str(mvp_table))[0]
    mvp['Year'] = year
    dfs.append(mvp)
mvps = pd.concat(dfs)
'''
'''mvps.to_csv('mvps.csv')'''
player_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

from selenium import webdriver

driver = webdriver.Chrome()
import time

'''for year in years:
    url = player_stats_url.format(year)

    driver.get(url)
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)

    html = driver.page_source
    with open('player/{}.html'.format(year),'w+',encoding="utf-8") as f:
        f.write(html)'''
'''dfs = []
for year in years:
    with open('player/{}.html'.format(year), 'r+', encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find(id='per_game_stats')
    player = pd.read_html(str(player_table))[0]
    player['Year'] = year
    dfs.append(player)
players = pd.concat(dfs)
players.to_csv('players.csv')'''

# division scraping
'''team_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_standings.html'
for year in years:
    url = team_stats_url.format(year)
    data = requests.get(url)
    with open('team/{}.html'.format(year), 'w+', encoding="utf-8") as f:
        f.write(data.text)'''
dfs = []
for year in years:
    with open('team/{}.html'.format(year), 'r+', encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    team_table = soup.find(id='divs_standings_E')
    team = pd.read_html(str(team_table))[0]
    team['Year'] = year
    team['Team'] = team['Eastern Conference']
    del team['Eastern Conference']
    dfs.append(team)

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    team_table = soup.find(id='divs_standings_W')
    team = pd.read_html(str(team_table))[0]
    team['Year'] = year
    team['Team'] = team['Western Conference']
    del team['Western Conference']
    dfs.append(team)
teams = pd.concat(dfs)
teams.to_csv('teams.csv')
