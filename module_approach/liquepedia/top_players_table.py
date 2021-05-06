import pandas, plotly.graph_objects as go

###a mudança aqui é equivalente à feita em game_popularity_heatmap

def create_table(game):
    path = "C:/Users/Usuario/Documents/module_approach/liquepedia/top_players_{}.csv".format(game)
    df = pandas.read_csv(path)
    names = df["Melhores Jogadores"][:5] #apenas os cinco primeiros elementos da coluna

    fig = go.Figure(data=[go.Table(header=dict(values=["Nome", "Posição"],
                                                fill_color = "white",
                                                line_color = "#ebf2ed",
                                                align = "left",
                                                height = 40
    ),
                    cells=dict(values=[names, ["1°", "2°", "3°", "4°", "5°"]],
                            line_color = "#ebf2ed",
                            fill_color = "white",
                            align = "left",
                            height = 35
                    ))
                        ])

    fig.update_layout(
        height=400,
        width = 500,
        title_text="Principais Jogadores do Competitivo ",
        title_x = 0.16
    )
    return fig

fig = create_table("lol")

if __name__ == "__main__":
    fig.show()
