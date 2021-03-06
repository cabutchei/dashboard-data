import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc #esta é uma componente do bootstrap(uma lib de css), tem q ser instalado previamente
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from steam import module
from steam.ccu_over_time_plot import fig as ccu_over_time 
from steam.top_games_by_ccu_plot import fig as top_games_by_ccu 
from steam.top_genres_plot import fig as top_genres
from twitch.top_games_twitch_pie_chart import fig as top_games1
from twitch.top_games_twitch_plot import fig as top_games3
from twitch.top_streamers_plot_express import fig  as top_streamers
from liquepedia.top_players_table import fig as top_players_table, create_table #criei as funções create_table e create_heatmap
from game_popularity.game_popularity_heatmap import fig as heatmap, create_heatmap #dentro dos arquivos originais a fim de facilitar
                                                                                    #as atualizações

settings = {  #configurações de tamanho para os gráficos, ajuste os parâmetros à vontade
    "ccu_over_time": {"graph": ccu_over_time, "width": 700, "height": 300},
    "top_games_by_ccu": {"graph": top_games_by_ccu, "width": None, "height": None},
    "top_genres": {"graph": top_genres, "width": 600, "height": 300},
    "top_games1": {"graph": top_games1, "width": 600, "height": None},
    "top_games3": {"graph": top_games3, "width": 700, "height": 450},
    "top_streamers": {"graph": top_streamers, "width": None, "height": 400},
    "top_players_table": {"graph": top_players_table, "width": 450, "height": 400},  #-------->tinha esquecido de incluir a tabela
    "heatmap": {"graph": heatmap, "width": 750, "height": 400, "coloraxis_showscale": False}
}

def apply_settings(figure = None, graph = None):  #esta função é responsável por aplicar os parâmetros escolhidos em settings
    if figure == None and graph != None:           #--------->pequena alteração na função para gastar menos linhas atualizando as configurações em update_figures
        return                                      #agora a função aceita também, como parâmetro opcional, um objeto do plotly. Também tirei o loop de dentro da função
    if graph == None:
        graph = settings[figure]["graph"]

    width = settings[figure]["width"]
    height = settings[figure]["height"]
    graph.update_layout(width = width, height = height)
    if figure == "heatmap":
        showscale = settings[figure]["coloraxis_showscale"]
        graph.update_layout(coloraxis_showscale = showscale)

for figure in settings:
    apply_settings(figure = figure)

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

navbar = dbc.Navbar( #essa é a navbar do site
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src="https://i.pinimg.com/originals/72/3d/0a/723d0af616b1fe7d5c7e56a3532be3cd.png", height="30px")),
                    #link para a logo da navbar
                    dbc.Col(dbc.NavbarBrand("Dashboard Game", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            )
        ),
        dbc.NavbarToggler(id="navbar-toggler")
    ],
    color = "white"
)


button_group = dbc.ButtonGroup(id = "buttons", children =  #grupo vertical de botões responsável pelas atualizações, posteriormente
    [                                                       #adicionado a uma das divs "middle" 
        dbc.Button("League of Legends", id = "lol", color = "light"),
        dbc.Button("Counter Strike: Global Offensive", id = "csgo", color = "light"),
        dbc.Button("Valorant", id = "valorant", color = "light"),  #------->troquei starcraft por valorant(quem liga pra starcraft?)
        dbc.Button("Dota 2", id = "dota2", color = "light"),
        dbc.Button("PUBG", id = "pubg", color = "light"),
        dbc.Button("Apex Legends", id = "apexlegends", color = "light"),
        dbc.Button("Call of Duty: Moden Warfare", id = "codmw", color = "light")
    ],
    vertical=True,
    style = {"position": "absolute", "top": 80, "width": 338}
)

app.layout = html.Div(className = "html", style = {"background-color": "#D5DFEE", "height": 2296}, children = [navbar,
#há um div mãe, que eu chamei de "html", é a div da página inteira. A div "body" se refere ao corpo da página(sem a navbar)
html.Div(className = "body", style = {"margin-top": 90, "margin-left": 100, "margin-right" : 100, "margin-bottom": 90}, children = [

html.Div(className = "top", style = {"position": "relative", "height": 300, "margin-bottom": 10}, children = [
    dcc.Graph( #ainda falta adicionar funcionalidade a esse gráfico. O objetivo é deixar a data à escolha do usuário
        id = "ccu_over_time",
        figure = ccu_over_time,
        style = {"position": "absolute"}
    ),
    dcc.Graph(
        figure = top_genres,
        style = {"position": "absolute", "right": 0}
    )
]),

html.Div(className = "middle", style = {"margin-bottom": 10}, children = [
    dcc.Graph(
        figure = top_games_by_ccu
    )


]),


html.Div(className = "middle", style = {"background-color": "white", "height": 420, "position": "relative", "margin-bottom": 10}, children = [
    dcc.Graph(
        id = "heatmap",
        figure = heatmap,
        style = {"position": "absolute", "top": 20, "left": 225}     
    ),
    button_group,
    
    dcc.Graph(
        id = "top_players",
        figure = top_players_table,
        style = {"position": "absolute", "right" : 0}
    )
]), 

html.Div(className = "bottom", style = {"position": "relative", "height": 450, "margin-bottom": 10}, children = [
    dcc.Graph(
        id = "top_games_twitch",
        figure = top_games3,
        style = {"position": "absolute", "left": 0}
    ),
    dcc.Graph(
        figure = top_games1,
        style = {"position": "absolute", "right": 0}
    
    )
]),

html.Div(className = "bottom", style = {"position": "relative", "height": 400}, children =
    dcc.Graph(
        figure = top_streamers
    )
)


])])

#essa função espera por um evento de clique e atualiza tanto o heatmap quanto a tabela. É uma callback
#que recebe 7 inputs(os 7 botões disponíveis) e retorna dois outputs, que inteferem, respectivamente com o heatmap e com a tabela.

@app.callback([Output(component_id = "heatmap", component_property  = "figure"),
Output(component_id = "top_players", component_property = "figure")], 
[Input(component_id = "lol", component_property = "n_clicks"),
Input(component_id = "csgo", component_property = "n_clicks"),
Input(component_id = "valorant", component_property = "n_clicks"),
Input(component_id = "dota2", component_property = "n_clicks"),
Input(component_id = "pubg", component_property = "n_clicks"),
Input(component_id = "apexlegends", component_property = "n_clicks"),
Input(component_id = "codmw", component_property = "n_clicks")])
def update_figures(button1, button2, button3, button4, button5, button6, button7):  #------->troquei o nome da função para fazer mais sentido
    _id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]  #------->decidi deixar de ser retardado e reduzi bastante o número de linhas aqui
    if not _id:
        raise PreventUpdate
    else:
        new_heatmap = create_heatmap(_id)
        new_table = create_table(_id)
    apply_settings("heatmap", new_heatmap)
    apply_settings("top_players_table", new_table)
    return new_heatmap , new_table


if __name__ == "__main__":
    app.run_server(debug = True)
