from bs4 import BeautifulSoup
import requests
import pandas as pd

years = list(range(2004,2023))
url_start = 'https://www.basketball-reference.com/awards/awards_{}.html'
for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open('mvp/{}.html'.format(year),'w+', encoding="utf-8") as f:
        f.write(data.text)

with open('mvp/2005.html') as g:
    page =g.read()
soup = BeautifulSoup(page,'html.parser')
soup.find('tr', class_='over_header').decompose()
mvp_table = soup.find_all(id='mvp')

mvp_1991 = pd.read_html(str(mvp_table))[0]
print(mvp_1991)


'''soup = BeautifulSoup(page,'html.parser')
soup.find_all(id='div_pgl_basic')'''