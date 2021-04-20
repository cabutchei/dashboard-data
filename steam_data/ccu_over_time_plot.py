import pandas
import plotly.express as px
from ccu_over_time import plot_data

data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv")[:8]
games = list(data["Nome"])
date = "19/04/2021" #parâmetro date pode ser escolhido livremente dentro do intervalo de tempo em que foram coletados os dados
title = "Evolução do número de jogadores simultâneos(ccu) no dia {}".format(date)
df = plot_data(games, date)
#df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_cc")

fig = px.line(df, x = "Hora", y = "ccu" , color= "Nome", hover_data = {"Hora": False})

fig.update_layout(title = title)

fig.show()
