import requests, pandas, json

url_top = "http://steamspy.com/api.php?request=top100in2weeks"
r1 = requests.get(url_top)
data = r1.json()
game_tags = {}

for game in data:
    url_game = "https://steamspy.com/api.php?request=appdetails&appid={}".format(game)
    r2 = requests.get(url_game)
    game_details = r2.json()
    game_name = game_details["name"]
    tags = []
    for tag in game_details["tags"]:
        tags.append(tag)
    game_tags[game_name] = tags

tag_count = {"RPG": 0, "Horror": 0, "Indie": 0, "MOBA": 0, "Arcade": 0, "FPS": 0, "Battle Royale": 0, "MMORPG": 0, "Party Game": 0}
for game in game_tags:
    for tag in game_tags[game]:
        if tag in tag_count:
            tag_count[tag] += 1

df = pandas.DataFrame(tag_count.items(), columns = ["Gênero", "Incidência"])
#df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/genres.csv", index = False)



