import plotly.express as px
import pandas, module
streamers_data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/twitchdata-update.csv")
def sort(df, column_name, reverse = False):
    d = []
    indexes = []
    for i in range(len(df)):
        d.append([df[column_name][i], i])
    d.sort(reverse = reverse, key = lambda x : x[0])
    for x in d:
        indexes.append(x[1])
    new_df = module.filter_by_row_and_column(df, indexes)
    return new_df
streamers_data = sort(streamers_data, "Average viewers", reverse = True)
streamers_data = module.filter_by_row_and_column(streamers_data, (0 , 9), ["Channel", "Average viewers", "Followers", "Language"])
streamers_data.rename(columns = {"Channel": "Canal", "Average viewers": "Visualização Média", "Followers": "Seguidores", "Language": "Idioma"}, inplace = True)

translation = {"English": "Inglês", "Portuguese": "Português", "Spanish": "Espanhol", "Korean": "Coreano", "Russian": "Russo"}
for i in range(10): #traduzindo os nomes dos idiomas para o português 
    language = streamers_data["Idioma"][i]
    streamers_data["Idioma"][i] = translation[language]

fig = px.scatter(streamers_data, x = "Canal", y = "Visualização Média", size = "Seguidores",
color = "Idioma", hover_name = "Canal" , size_max  = 200, title = "Top streamers por visualização média")
fig.show()
