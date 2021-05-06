import pandas, module
import plotly.express as px

##mudanças nesse script: como no heatmap e no top_players, aqui também foi criada uma função que gera o gráfico. Nesse caso o argumento
##da função é a data. Essa função pode ser importada futuramente pelo dashboard para atualizar o ccu_over_time

def create_ccu_plot(date):#parâmetro date pode ser escolhido livremente dentro do intervalo de tempo em que foram coletados os dados
                          #infelizmente, há um gap nos dados entre às 18 do dia 21 e às 10 do dia seguinte porque o código parou de rodar
    top_games = pandas.read_csv("C:/Users/Usuario/Documents/module_approach/steam/top_games_by_ccu.csv")
    top_games_stats = pandas.read_csv("C:/Users/Usuario/Documents/module_approach/steam/top_games_by_ccu_stats.csv")
    top8 = module.filter_by_row_and_column(top_games_stats, rows = (0,7)).Nome
    title = "Evolução do número de jogadores simultâneos(ccu) no dia {}".format(date)

    df = module.filter_by_date(top_games, "Hora", date)
    df = module.filter_by_name(df, "Nome", top8)
    df = module.to_hours(df, "Hora")

    fig = px.line(df, x = "Hora", y = "ccu" , color= "Nome", hover_data = {"Hora": False})

    fig.update_layout(title = title, plot_bgcolor = "white")

    fig.update_xaxes(dtick = 2)
    return fig

fig = create_ccu_plot("23/04/2021")

if __name__ == "__main__":
    fig.show() 
 

