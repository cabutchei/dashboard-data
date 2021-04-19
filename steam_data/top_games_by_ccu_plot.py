##Esse script faz o plot com os dados obtidos da média de jogadores concorrentes de cada jogo

import plotly.graph_objects as go
import pandas

data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv") 
games = list(data["Nome"])[:8] #lista com os nomes
games.reverse() #o reverse se faz necessário para que o plotly disponha os primeiros colocados na parte de cima
average_ccu = list(data["Média de ccu"])[:8]
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


def layout(name, ccu): #layout seta um dado jogo no gráfico junto com sua boxart de acordo com os parâmetros informados
    formatted = name.replace(" ", "%20")
    if name == "Source SDK Base 2013 Multiplayer":
        source = "https://res-3.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco/b17gr3xreillrivarc3d"
    else:
        source = "https://static-cdn.jtvnw.net/ttv-boxart/{}-100x100.jpg".format(formatted)
    fig.add_layout_image(
        dict(
            source = source,
            xref="x",
            yref="y",
            x = ccu,
            y = name,
            yanchor = "middle",
            xanchor = "left",
            sizex = 50000,
            sizey = 0.85
        )
)


for i in range(8):
    layout(games[i], average_ccu[i])



fig.show()
