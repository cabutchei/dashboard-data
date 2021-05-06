import requests, pandas, json

url_top = "http://steamspy.com/api.php?request=top100in2weeks"
r1 = requests.get(url_top)
data = r1.json() #data é um dicionário cujas chaves são as id's de cada jogo
game_tags = {}


for game in data: #itera sobre cada jogo em data e para cada jogo faz um request à api
    url_game = "https://steamspy.com/api.php?request=appdetails&appid={}".format(game) #a variável game guarda a id do jogo analisado
    r2 = requests.get(url_game)
    game_details = r2.json() #dicionário com os detalhes do jogo relativo à corrente iteração
    game_name = game_details["name"]
    tags = [] #lista com todas as tags de todos os jogos em data
    for tag in game_details["tags"]: #adicionar todas as tags referentes a cada jogo
        tags.append(tag)
    game_tags[game_name] = tags #criar uma chave para cada jogo, os valores são a lista tags

tag_count = {"RPG": 0, "Horror": 0, "Indie": 0, "MOBA": 0, "Arcade": 0, "FPS": 0, "Battle Royale": 0, "MMORPG": 0, "Party Game": 0}
for game in game_tags:  #loop duplo, itera sobre cada tag de cada jogo
    for tag in game_tags[game]:
        if tag in tag_count: #para cada match, incrementar a contagem em tag_count
            tag_count[tag] += 1

df = pandas.DataFrame(tag_count.items(), columns = ["Gênero", "Incidência"])
print(df)
#df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_genres_2_weeks.csv", index = False)



