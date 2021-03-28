import pandas, requests
from bs4 import BeautifulSoup

url = "https://liquipedia.net/counterstrike/Rankings/2020#Players"

html_text = requests.get(url).content

soup = BeautifulSoup(html_text, "html.parser")

table = soup.find("table")

tr = table.find_all("tr")[1:]

td = []

for i in range(len(tr)):
    td += tr[i].find_all("td", limit = 2)

names = []

for i in range(len(td)//2):
    names.append([td[2 * i + 1].text[:-2]])

data = pandas.DataFrame(names, columns= ["Melhores Jogadores"])

data.to_csv("top_players_cs.csv")