import plotly.graph_objects as go
import pandas

data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv") 
games = list(data["Nome"])[:8] #lista com os nomes
games.reverse() #o reverse se faz necessário para que o plotly disponha os primeiros colocados na parte de cima
average_views = list(data["Visualização Média"])[:8] #<--atualizado
average_views.reverse() #<--atualizado
average_views = list(map(lambda view : "Visualização Média: " + str(view), average_views)) #<--atualizado
percentages = list(map(lambda percentage : float(percentage[:-1]), data["Frequência no Top 3"]))[:8] #fazer lista com as porcentagens,
percentages.reverse()                                                                           #eliminando o "%" e convertendo em float

fig = go.Figure()

fig.add_trace(go.Bar(
    y= games, #os nomes comporão a ordenada e as porcentagens, a abscissa
    x=percentages,
    text = average_views, #<--atualizado
    orientation='h', #vertical ou horizontal
    marker=dict(
        color='#9803fc', #cor da barra
        line=dict(color='#9803fc', width=3) #cor da borda da barra
    )
))

fig.update_layout(title = "Games mais populares da twitch por frequência no top 3", #<--atualizado
        paper_bgcolor = 'white',
                plot_bgcolor = 'white')


def layout(name, percentage): #layout seta um dado jogo no gráfico junto com sua boxart de acordo com os parâmetros informados
    formatted = name.replace(" ", "%20")
    source = "https://static-cdn.jtvnw.net/ttv-boxart/{}-100x100.jpg".format(formatted)
    fig.add_layout_image(
        dict(
            source = source,
            xref="x",
            yref="y",
            x = percentage,
            y = name,
            yanchor = "middle",
            xanchor = "left",
            sizex = 5,
            sizey = 0.85
        )
)


for i in range(8):
    layout(games[i], percentages[i])



fig.show()
