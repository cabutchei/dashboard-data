import plotly.express as px
import pandas
streamers_data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/twitchdata-update.csv")
streamers_data = streamers_data.filter(items = ["Channel", "Average viewers", "Followers", "Language"])
streamers_data = streamers_data.sort_values(by = ["Average viewers"], ascending = False)[0:10] #ascending = False sorteia de maniera descendente
streamers_data.rename(columns = {"Channel": "Canal", "Average viewers": "Visualização Média", "Followers": "Seguidores", "Language": "Idioma"}, inplace = True)
streamers_data.reset_index(inplace = True, drop = True) #inplace = True faz a modificação no df original, drop = True evita que os indexes antigos virem uma nova coluna 

translation = {"English": "Inglês", "Portuguese": "Português", "Spanish": "Espanhol", "Korean": "Coreano", "Russian": "Russo"}
for i in range(10): #traduzindo os nomes dos idiomas para o português 
    language = streamers_data["Idioma"][i]
    streamers_data["Idioma"][i] = translation[language]


fig = px.scatter(streamers_data, x = "Canal", y = "Visualização Média", size = "Seguidores",
color = "Idioma", hover_name = "Canal" , size_max  = 200, title = "Top streamers por visualização média")
fig.show()