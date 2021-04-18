### Este script retorna automaticamente as tabelas em csv de boa parte dos jogos na liquepedia.
### Não há tabela para Overwatch. Para Starcraft II, CS, ou Rocket League, referir-se aos outros scripts.

import pandas, requests
from bs4 import BeautifulSoup

def game_url(game):
    return "https://liquipedia.net/{}/Portal:Statistics".format(game)

game = input()

    
url = game_url(game)

page = requests.get(url)

if page.status_code == 404:
    raise Exception("Invalid URL")

html_text = page.content


soup = BeautifulSoup(html_text, "html.parser")
span = soup.find(id = "By_player")

h3 = span.parent

div = h3.next_sibling.next_sibling.find("tbody")

table = div.find_all("tr")[1:]

table_names = []

number_of_players = len(table)

for i in range(number_of_players):
    table_names.append([table[i].find_all("a")[1].text])

data = pandas.DataFrame(table_names , columns = ["Melhores Jogadores"])

print(data)

#data.to_csv("data.csv", index = False)

