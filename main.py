from bs4 import BeautifulSoup
import requests
import pandas as pd

years = list(range(1991,2021))
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

for year in years:
    url = player_stats_url.format(year)

    driver.get(url)
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)

    html = driver.page_source
    with open('player/{}.html'.format(year),'w+',encoding="utf-8") as f:
        f.write(html)



