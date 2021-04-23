import plotly.graph_objects as go
import pandas, module

df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv")
df = module.filter_by_row_and_column(df, (0,7))
games = list(df["Nome"]) #lista com os nomes
games.reverse() #o reverse se faz necessário para que o plotly disponha os primeiros colocados na parte de cima
average_ccu = list(df["Média de ccu"])
average_ccu.reverse()



fig = go.Figure()

fig.add_trace(go.Bar(
    y= games, #os nomes comporão a ordenada e as porcentagens, a abscissa
    x=average_ccu,
    orientation='h', #vertical ou horizontal
    marker=dict(
        color='#1b0261', #cor da barra
        line=dict(color='#1b0261', width=3) #cor da borda da barra
    )
))

fig.update_layout(title = "Top games da Steam por jogadores simultâneos",
        paper_bgcolor = 'white',
                plot_bgcolor = 'white')



for i in range(8):
    module.layout(fig, average_ccu[i], games[i], 50000)



fig.show()