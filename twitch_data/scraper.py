import requests, pandas, json, datetime, time

access_token = None
client_id = None

url_games = "https://api.twitch.tv/helix/games/top?first=9"
headers = {"Authorization": "Bearer " + access_token,
"Client-Id": client_id
}

for iteration in range(170):

    time = datetime.datetime.now()
    timestamp = time.strftime("%d/%m/%Y %H:%M") #formatação do timestamp em dia/mês/ano, hora:minutos

    r1 = requests.get(url_games, headers = headers)

    data_games = r1.json()["data"] #lista de dicionários relativa aos jogos
    data_streams = [] #futura lista de dicionários relativa às streams
    games = [] #futura lista de listas, corresponde às linhas do dataframe

    for game in data_games:  #excluir a tag Just Chatting por não se tratar de jogo
        if game["name"] == "Just Chatting":
            i = data_games.index(game)
            del data_games[i]
            break


    for game in data_games:  #checar as streams ativas no momento em relação a cada jogo
        parameter = "&game_id=" + game["id"]
        for i in range(10):  #checando 10 páginas de resultado por jogo(ou até a última página caso sejam menos que 10)
            if i == 0:
                url_streams = "https://api.twitch.tv/helix/streams?first=100"
                url_streams += parameter
            else:
                url_streams = "https://api.twitch.tv/helix/streams?first=100"
                parameter += "&after={}".format(pagination) #o identificador pagination é usado para retornar a próxima página de resultados
                url_streams += parameter
            r2 = requests.get(url_streams, headers = headers)
            stream_json = r2.json() 
            data_streams += stream_json["data"] #adicionar o dicionário de streams à lista data_streams
            try: #lida com o possível erro de não haver mais páginas resultados antes do fim da corrente iteração
                pagination = stream_json["pagination"]["cursor"]
            except:
                break


    for game in data_games:  #fazer contagem total de viewers e canais para cada jogo e adicionar aos dicionários
        game["viewers"] = 0
        game["channels"] = 0
        for stream in data_streams:
            if stream["game_id"] == game["id"]:
                game["viewers"] += stream["viewer_count"]
                game["channels"] += 1


    for game in data_games:  #adicionar os dados relevantes de cada jogo à lista games
        games.append([timestamp, game["name"], game["viewers"], game["channels"]])

    columns = ["Hora","Nome", "Visualizações", "Canais"]

    df = pandas.DataFrame(games, columns=columns)
    df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_from_past_week.csv", mode = "a", header = False, index = False)
    #modo "a" para "append", adiciona o resultado ao final do arquivo já existente
    if iteration % 50 == 0:
        print("Everything's working")
    time.sleep(3600) #o loop ocorre a cada hora

