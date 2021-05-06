import plotly.graph_objects as go
import pandas, module

data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv")[:8]
games = list(data["Nome"]) #lista com os nomes
games.reverse() #o reverse se faz necessário para que o plotly disponha os primeiros colocados na parte de cima
average_views = list(data["Visualização Média"])
average_views.reverse()
average_views = list(map(lambda view : "Visualização Média: " + str(view), average_views))
percentages = list(map(lambda percentage : float(percentage[:-1]), data["Frequência no Top 3"])) #fazer lista com as porcentagens,
percentages.reverse()                                                                           #eliminando o "%" e convertendo em float


fig = go.Figure()

fig.add_trace(go.Bar(
    y= games, #os nomes comporão a ordenada e as porcentagens, a abscissa
    x=percentages,
    text = average_views,
    orientation='h', #vertical ou horizontal
    marker=dict(
        color='#9803fc', #cor da barra
        line=dict(color='#9803fc', width=3) #cor da borda da barra
    )
))

fig.update_layout(title = "Top games da twitch por frequência no top 3",
        paper_bgcolor = 'white',
                plot_bgcolor = 'white')


for i in range(8):
    module.layout(fig, percentages[i], games[i], 5)


if __name__ == "__main__":
    fig.show()