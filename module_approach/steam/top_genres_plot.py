import plotly.graph_objects as go
import pandas

df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_genres_2_weeks.csv")  

genre = df["Gênero"]
occurrences = df["Incidência"]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=occurrences,
    y=genre,
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line_color='rgba(156, 165, 196, 1.0)',
    )
))

fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

fig.update_layout(
    title="Gêneros mais populares das últimas duas semanas",
    xaxis=dict(
        showgrid=False, #mostrar as linhas do grid
        showline=False, #mostrar a linha do eixo x
        tickfont_color='rgb(102, 102, 102)', #cor da fonte dos números no eix x
        showticklabels=True, #mostrar a identificação(número) correspondente às barrinhas do eixo x
        dtick=10, #espaço entre os números mostrados
        ticks='outside', #posição das barrinhas da linha inferior
        tickcolor='rgb(102, 102, 102)', #cor das barrinhas
    ),
    margin=dict(l=140, r=40, b=50, t=80),

    width=800,
    height=600,
    paper_bgcolor='white', 
    plot_bgcolor='white', 
    hovermode='closest', 
)
fig.show()
