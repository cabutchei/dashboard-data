import plotly.express as px
import pandas, module
streamers_data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/twitchdata-update.csv")

streamers_data = module.sort(streamers_data, "Average viewers", reverse = True)
streamers_data = module.filter_by_row_and_column(streamers_data, (0 , 9), ["Channel", "Average viewers", "Followers", "Language"])
streamers_data.rename(columns = {"Channel": "Canal", "Average viewers": "Visualização Média", "Followers": "Seguidores", "Language": "Idioma"}, inplace = True)

translation = {"English": "Inglês", "Portuguese": "Português", "Spanish": "Espanhol", "Korean": "Coreano", "Russian": "Russo"}
for i in range(10): #traduzindo os nomes dos idiomas para o português 
    language = streamers_data["Idioma"][i]
    streamers_data["Idioma"][i] = translation[language]

fig = px.scatter(streamers_data, x = "Canal", y = "Visualização Média", size = "Seguidores",
color = "Idioma", hover_name = "Canal" , size_max  = 200, title = "Top streamers por visualização média")

fig.update_layout(paper_bgcolor = "white", plot_bgcolor = "white")

if __name__ == "__main__":
    fig.show()
