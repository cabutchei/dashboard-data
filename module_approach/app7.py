import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc #esta é uma componente do bootstrap(uma lib de css), tem q ser instalado previamente
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from steam import module
from steam.ccu_over_time_plot import fig as ccu_over_time, create_ccu_plot 
from steam.top_games_by_ccu_plot import fig as top_games_by_ccu 
from steam.top_genres_plot import fig as top_genres
from twitch.top_games_twitch_pie_chart import fig as top_games1
from twitch.top_games_twitch_plot import fig as top_games3
from twitch.top_streamers_plot_express import fig  as top_streamers
from liquepedia.top_players_dash_table import table as top_players_table, create_table_ #criei as funções create_table e create_heatmap
from game_popularity.game_popularity_heatmap import fig as heatmap, create_heatmap #dentro dos arquivos originais a fim de facilitar
                                                                                    #as atualizações

settings = {  #configurações de tamanho para os gráficos, ajuste os parâmetros à vontade
    "ccu_over_time": {"graph": ccu_over_time, "width": 700, "height": 300},
    "top_games_by_ccu": {"graph": top_games_by_ccu, "width": None, "height": None},
    "top_genres": {"graph": top_genres, "width": 600, "height": 300},
    "top_games1": {"graph": top_games1, "width": 600, "height": None},
    "top_games3": {"graph": top_games3, "width": 700, "height": 450},
    "top_streamers": {"graph": top_streamers, "width": None, "height": 400},
    # "top_players_table": {"graph": top_players_table, "width": 450, "height": 400},  #-------->tinha esquecido de incluir a tabela
    "heatmap": {"graph": heatmap, "width": 750, "height": 400, "coloraxis_showscale": False}
}

color_settings = {
    "dark": False,
    "figures": {
       "ccu_over_time": {"graph": ccu_over_time, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "top_games_by_ccu": {"graph": top_games_by_ccu, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "top_genres": {"graph": top_genres, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "top_games1": {"graph": top_games1, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "top_games3": {"graph": top_games3, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "top_streamers": {"graph": top_streamers, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None},
       "heatmap": {"graph": heatmap, "font_color": None, "paper_bgcolor": None, "plot_bgcolor": None}
    },
    "html": {
        "navbar_color": "white",
        "page_bgcolor": "#D5DFEE",
        "div_bgcolor": "white",
        "top_players_table": {"style_header": {"backgroundColor": "white"}, "style_cell": {"backgroundColor": "white", "color": None}}
    }
}

def update_colors(dark):
    figures = color_settings["figures"].values()
    html = color_settings["html"]
    if not dark: 
        for figure in figures:
            figure["font_color"] = "#90b4ce"
            figure["paper_bgcolor"] = "#1c1c24"
            figure["plot_bgcolor"] = "#1c1c24"
        html["navbar_color"] = "#1c1c24"
        html["page_bgcolor"] = "#000000" 
        html["div_bgcolor"] = "#1c1c24"
        html["top_players_table"] = {"style_header": {"backgroundColor": "#1c1c24"}, "style_cell": {"backgroundColor": "#1c1c24", "color": "white"}}
    else:
        for figure in figures:
            figure["font_color"] = None
            figure["paper_bgcolor"] = "white"
            figure["plot_bgcolor"] = "white"
        html["navbar_color"] = "white"
        html["page_bgcolor"] = "#D5DFEE"
        html["div_bgcolor"] = "white"
        html["top_players_table"] = {"style_header": {"backgroundColor": "white"}, "style_cell": {"backgroundColor": "white", "color": None}}
    return not dark

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

def apply_color_settings(color_settings):
    for figure in color_settings["figures"].values():
        graph = figure["graph"]
        font_color = figure["font_color"]
        paper_bgcolor = figure["paper_bgcolor"]
        plot_bgcolor = figure["plot_bgcolor"]
        graph.update_layout(font_color = font_color, paper_bgcolor = paper_bgcolor, plot_bgcolor = plot_bgcolor)

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

navbar = dbc.Navbar( #essa é a navbar do site
    id = "navbar",
    children = [
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
    color = color_settings["html"]["navbar_color"],
    dark = False

)

dark_button = dbc.Button("Light", id = "ButaoEscuro", color = "light", className = "mr-1",
    style = {"position": "absolute", "right": 0, "top": 62}
    
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

dropdown = dbc.DropdownMenu(
    id = "bbb",
    label="Data",
    style = {"position": "absolute", "left": 500, "top": 225},
    color = "light",
    children = [
        dbc.DropdownMenuItem("19/04/2021", id = "19/04/2021"),
        dbc.DropdownMenuItem("20/04/2021", id = "20/04/2021"),
        dbc.DropdownMenuItem("21/04/2021", id = "21/04/2021"),
        dbc.DropdownMenuItem("22/04/2021", id = "22/04/2021"),
        dbc.DropdownMenuItem("23/04/2021", id = "23/04/2021"),
        dbc.DropdownMenuItem("24/04/2021", id = "24/04/2021"),
        dbc.DropdownMenuItem("25/04/2021", id = "25/04/2021"),
    ],    
)    

app.layout = html.Div(id = "page", className = "html", style = {"background-color": color_settings["html"]["page_bgcolor"], "height": 2296}, children = [navbar,
dark_button,
html.Div(className = "body", style = {"margin-top": 90, "margin-left": 100, "margin-right" : 100, "margin-bottom": 90}, children = [

html.Div(className = "top", style = {"position": "relative", "height": 300, "margin-bottom": 10}, children = [
    dcc.Graph( #ainda falta adicionar funcionalidade a esse gráfico. O objetivo é deixar a data à escolha do usuário
        id = "ccu_over_time",
        figure = ccu_over_time,
        style = {"position": "absolute"}
    ),
    dcc.Graph(
        id = "top_genres",
        figure = top_genres,
        style = {"position": "absolute", "right": 0}
    ),
    dropdown
]),

html.Div(className = "middle", style = {"margin-bottom": 10}, children = [
    dcc.Graph(
        id = "top_games_by_ccu",
        figure = top_games_by_ccu
    )


]),


html.Div(id = "heatmap_div", className = "middle", style = {"background-color": color_settings["html"]["div_bgcolor"], "height": 420, "position": "relative", "margin-bottom": 10}, children = [
    dcc.Graph(
        id = "heatmap",
        figure = heatmap,
        style = {"position": "absolute", "top": 20, "left": 225}     
    ),
    button_group,

    html.Div(
        id = "top_players_table",
        children = top_players_table,
        style = {"position": "absolute", "right": 0, "top": 100}
    )
]), 

html.Div(className = "bottom", style = {"position": "relative", "height": 450, "margin-bottom": 10}, children = [
    dcc.Graph(
        id = "top_games3",
        figure = top_games3,
        style = {"position": "absolute", "left": 0}
    ),
    dcc.Graph(
        id = "top_games1",
        figure = top_games1,
        style = {"position": "absolute", "right": 0}
    
    )
]),

html.Div(className = "bottom", style = {"position": "relative", "height": 400}, children =
    dcc.Graph(
        id = "top_streamers",
        figure = top_streamers
    )
)


])])

#essa função espera por um evento de clique e atualiza tanto o heatmap quanto a tabela. É uma callback
#que recebe 7 inputs(os 7 botões disponíveis) e retorna dois outputs, que inteferem, respectivamente com o heatmap e com a tabela.

@app.callback([Output(component_id = "ccu_over_time", component_property = "figure"),
Output(component_id = "top_games_by_ccu", component_property = "figure"),  
Output(component_id = "top_genres", component_property = "figure"), 
Output(component_id = "top_games1", component_property = "figure"),  
Output(component_id = "top_games3", component_property = "figure"),  
Output(component_id = "top_streamers", component_property = "figure"),
Output(component_id = "top_players_table", component_property = "children"),
Output(component_id = "top_players_table_object", component_property = "style_header"),
Output(component_id = "top_players_table_object", component_property = "style_cell"),
Output(component_id = "heatmap", component_property  = "figure"),
Output(component_id = "navbar", component_property = "color"),
Output(component_id = "navbar", component_property = "dark"),
Output(component_id = "page", component_property = "style"),
Output(component_id = "heatmap_div", component_property = "style")],
[Input(component_id = "19/04/2021", component_property = "n_clicks"),
Input(component_id = "20/04/2021", component_property = "n_clicks"),
Input(component_id = "21/04/2021", component_property = "n_clicks"),
Input(component_id = "22/04/2021", component_property = "n_clicks"),
Input(component_id = "23/04/2021", component_property = "n_clicks"),
Input(component_id = "24/04/2021", component_property = "n_clicks"),
Input(component_id = "25/04/2021", component_property = "n_clicks"),
Input(component_id = "lol", component_property = "n_clicks"),
Input(component_id = "csgo", component_property = "n_clicks"),
Input(component_id = "valorant", component_property = "n_clicks"),
Input(component_id = "dota2", component_property = "n_clicks"),
Input(component_id = "pubg", component_property = "n_clicks"),
Input(component_id = "apexlegends", component_property = "n_clicks"),
Input(component_id = "codmw", component_property = "n_clicks"),
Input(component_id = "ButaoEscuro", component_property = "n_clicks")])
# def update_figures(button1, button2, button3, button4, button5, button6, button7):  #------->troquei o nome da função para fazer mais sentido
#     _id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]  #------->decidi deixar de ser retardado e reduzi bastante o número de linhas aqui
#     if not _id:
#         raise PreventUpdate
#     else:
#         new_heatmap = create_heatmap(_id)
#         new_table = create_table(_id)
#     apply_settings("heatmap", new_heatmap)
#     apply_settings("top_players_table", new_table)
#     return new_heatmap , new_table
def update_figures(date1, date2, date3, date4, date5, date6, date7, game1, game2, game3, game4, game5, game6, game7, dark_button):  #------->troquei o nome da função para fazer mais sentido
    _id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]  #------->decidi deixar de ser retardado e reduzi bastante o número de linhas aqui
    if not _id:
        raise PreventUpdate
    else:
        games = ["lol", "csgo", "valorant", "dota2", "pubg", "apexlegends", "codmw"]
        dates = ["19/04/2021", "20/04/2021", "21/04/2021", "22/04/2021", "23/04/2021", "24/04/2021", "25/04/2021"]
        if _id in games:
            new_heatmap = create_heatmap(_id)
            new_table = create_table_(_id, color_settings["html"]["top_players_table"])
            apply_settings("heatmap", new_heatmap)
            return new_heatmap , new_table
        elif _id in dates:
            new_OitoOito = create_ccu_plot(_id)
            apply_settings("ccu_over_time", new_OitoOito)
            return new_OitoOito
        elif _id == "ButaoEscuro":
            dark = update_colors(color_settings["dark"])
            color_settings["dark"] = dark
            apply_color_settings(color_settings)
            navbar_color = color_settings["html"]["navbar_color"]
            navbar_dark = dark
            style_page = {"background-color": color_settings["html"]["page_bgcolor"], "height": 2296}
            style_div = {"background-color": color_settings["html"]["div_bgcolor"], "height": 420, "position": "relative", "margin-bottom": 10}
            table_style_header = {"height": 40, "backgroundColor": color_settings["html"]["top_players_table"]["style_header"]["backgroundColor"]}
            table_style_cell = {"textAlign": "left", "backgroundColor": color_settings["html"]["top_players_table"]["style_cell"]["backgroundColor"],
            "color": color_settings["html"]["top_players_table"]["style_cell"]["color"]}
            return ccu_over_time, top_games_by_ccu, top_genres, top_games1, top_games3, top_streamers, top_players_table, table_style_header, table_style_cell, heatmap, navbar_color, navbar_dark, style_page, style_div


      
if __name__ == "__main__":
    app.run_server(debug = True)



