years = list(range(1991,2022))
url_start = 'https://www.basketball-reference.com/awards/awards_{}.html'

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

prefix .format pozwala na wstawienie wartości z range przy iterowaniu w loopie

linijka "url = url_start.format(year)" pozwala na wygenerowanie pełnego urla strony
linijka "data = requests.get(url)" metoda wysyłająca GET request do strony internetowej o wybranym url
                                    metoda ta zwraca tzw. status code

biblioteka request wysyła żądanie GET które pobiera zawartość HTML ze strony
status_code = 200 oznacza sukces w pobieraniu strony


with open('mvp/{}.html'.format(year), 'w+', encoding="utf-8") as f:
    f.write(data.text)

powyższe linijki to loop w zasięgu wybranych lat, dla każdego roku i jego url tworzymy plik
o formacie .html. Każdy plik jest tworzony w momencie iteracji,od razu wpisujemy do niego
status code(data) przy użyciu ".write", kod html musi zostać przetworzony w czytelny tekst,
uzywamy w tym celu metody .text

with open('mvp/2005.html') as f:
    page =f.read()

tutaj otwieramy utworzone pliki w trybie do odczytu, żeby przygotować je do beautifulsoup
metoda .read zwraca określoną liczbę bitów z pliku. Docelowo wartość ta wynosi -1, oznacza
odczyt całego pliku

soup = BeautifulSoup(page,'html.parser')
#inicjalizacja klasy beautifulsoup i jej egzemplarza- soup. Soup tworzymy jako parser html,
#który będzie czytał zawartość page i pozwoli na ekstrakcję tabelki

soup.find('tr', class_='over_header').decompose()
#szukamy w plikach elementów o tagu 'tr'z klasą "nagłówek- overheader"

#metoda .decompose() pozwala na usunięcie znalezionych elementów

mvp_table = soup.find(id='mvp')

#następnie wyciągamy tabelę po id które ma wartość "mvp"

mvp_1991 = pd.read_html(str(mvp_table))
#korzystamy z pandas, która może odczytywać html, ale musimy go odczytać jako string
#stąd też str()

#otrzymujemy listę dataframeów, żeby wyodrębnić jeden używamy indeksów
mvp_1991 = pd.read_html(str(mvp_table))[0]

dfs.append(mvp)

mvps = pd.concat(dfs)
#powstaje lista dataframeów, nie jest to korzystne rozwiązanie dlatego robimy z niej jedne dataframe

mvps.to_csv('mvps.csv')
#przerzucamy na csv


Z czego składa się strona internetowa?
Kiedy wszedłeś na stronę z tym artykułem to Twoja przeglądarka wysłała żądanie do serwera internetowego, by pobrać zawartość.  Następnie serwer odesłał Ci odpowiednie pliki, by prawidłowo wyświetlić stronę. Pliki można z grubsza podzielić na:

HTML – zawierają główną część strony,
CSS – tutaj jest zdefiniowany wygląd (np. style czcionki, akapitów itp.),
Zdjęcia – po prostu wszelkiego rodzaju grafiki, aby umożliwić wyświetlenie obrazów,
JS – pliki Javascript dodające interaktywność na stronie.


23.12.2023
pierwsze użycie selenium





