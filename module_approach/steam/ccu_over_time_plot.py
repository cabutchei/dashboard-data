import pandas, module
import plotly.express as px

top_games = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu - Copy.csv")
top_games_stats = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv")
top8 = module.filter_by_row_and_column(top_games_stats, rows = (0,7)).Nome
date = "19/04/2021" #parâmetro date pode ser escolhido livremente dentro do intervalo de tempo em que foram coletados os dados
title = "Evolução do número de jogadores simultâneos(ccu) no dia {}".format(date)

df = module.filter_by_date(top_games, "Hora", date)
df = module.filter_by_name(df, "Nome", top8)
df = module.to_hours(df, "Hora")

fig = px.line(df, x = "Hora", y = "ccu" , color= "Nome", hover_data = {"Hora": False})

fig.update_layout(title = title)

fig.update_xaxes(dtick = 2)

fig.show()


