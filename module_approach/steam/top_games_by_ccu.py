import requests, pandas, datetime, time
from bs4 import BeautifulSoup

for j in range(240):
    url = "https://store.steampowered.com/stats/Steam-Game-and-Player-Statistics"
    r = requests.get(url).content
    current_time = datetime.datetime.now()
    timestamp = time.strftime("%d/%m/%Y %H:%M")
    soup = BeautifulSoup(r, "html.parser")
    div = soup.find(id = "detailStats")
    table = div.contents[1]
    tr = table.find_all("tr", limit = 10)[2:]
    a = table.find_all("a")[:8]
    names = [x.text for x in a]
    numbers = []
    for element in tr:
        number = element.contents[1].text[1:-1]
        number = int(number.replace(",", ""))
        numbers.append(number)
    rows = []
    for i in range(8):
        rows.append([timestamp, names[i], numbers[i]])
    df = pandas.DataFrame(rows, columns = ["Hora", "Nome", "ccu"])
    df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu.csv", index = False, header = False, mode = "a")
    time.sleep(1800)