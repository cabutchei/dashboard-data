import pandas, plotly.graph_objects as go

game = "dota2"
path = "C:/Users/Usuario/Documents/Visual Studio Code/dashboard/data_from_liquepedia/top_players_{}.csv".format(game)
df = pandas.read_csv(path)
names = df["Melhores Jogadores"][:5] #apenas os cinco primeiros elementos da coluna

fig = go.Figure(data=[go.Table(header=dict(values=["Nome", "Posição"],
                                            fill_color = "white",
                                            line_color = "#ebf2ed",
                                            align = "left"
),
                 cells=dict(values=[names, ["1°", "2°", "3°", "4°", "5°"]],
                           line_color = "#ebf2ed",
                           fill_color = "white",
                           align = "left" 
                 ))
                     ])

fig.update_layout(
    height=1000,
    width = 500,
    title_text="Principais Jogadores do Competitivo ",
    title_x = 0.16
)


fig.show()
