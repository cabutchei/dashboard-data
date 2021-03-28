import requests, pandas, json

access_token = None
client_id = None

headers = {
    "Authorization": "Bearer " + access_token ,
    'Client-Id': client_id
}

r = requests.get('https://api.twitch.tv/helix/games/top', headers=headers)

data = r.json()["data"]

games = []

for item in data:
    games.append(list(item.values()))

columns = ["id", "Name", "Box art url"]

df = pandas.DataFrame(games, columns = columns)

#df.to_csv("top_games.csv")

#print(df)

