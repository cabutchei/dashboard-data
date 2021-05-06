import plotly.express as px
import pandas

###novidades nesse código: o gráfico é criado pela função create_heatmap que tem como argumento o nome do jogo(de acordo com o nome do arquivo)
###isso possibilita que o dashboard importe essa função e facilmente crie um outro gráfico apenas mudando o argumento
 
def create_heatmap(game):
    path = "C:/Users/Usuario/Documents/module_approach/game_popularity/popularity_en/{}.csv".format(game)
    pop = pandas.read_csv(path)
    iso = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/game_popularity/countries_iso_rectified.csv")
    iso_dic = {} #dicionário que relaciona os países a seus códigos iso

    for i in range(252):
        iso_dic[iso.Country[i]] = iso.ISO[i]

    iso_column = [] #coluna com códigos iso, eles aparecerão na mesma ordem que os países em pop 

    for country in pop.Country:
        iso_column.append(iso_dic[country])

    iso_df = pandas.DataFrame(iso_column, columns=["ISO"])

    df = pandas.concat([pop, iso_df], axis=1) #concatenar horizontalmente os dois dataframes


    fig = px.choropleth(df, locations="ISO",
                        color="Popularity",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma)

    fig.update_layout(title = "Popularidade por país", title_xanchor = "left", title_x = 0.18)
    return fig

fig = create_heatmap("lol")

if __name__ == "__main__":
    #fig.show()
    print(fig)