from bs4 import BeautifulSoup
import requests
import pandas as pd

years = list(range(1991,2022))
url_start = 'https://www.basketball-reference.com/awards/awards_{}.html'

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open('mvp/{}.html'.format(year),'w+', encoding="utf-8") as f:
        f.write(data.text)

for year in years:
    dfs = []
    with open('mvp/{}.html'.format(year)) as f:
        page=f.read()
    soup = BeautifulSoup(page,'html.parser')
    #soup.find('tr', class_='over_header').decompose()
    mvp_table = soup.find(id='mvp')
    mvp = pd.read_html(str(mvp_table))[0]
    dfs.append(mvp)
mvps = pd.concat(dfs)

mvps.to_csv('mvps.csv')



'''soup = BeautifulSoup(page,'html.parser')
soup.find_all(id='div_pgl_basic')'''