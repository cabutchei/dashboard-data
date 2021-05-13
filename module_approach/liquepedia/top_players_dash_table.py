def create_table_(game, color_settings = {"style_header": {"backgroundColor": "white"}, "style_cell": {"backgroundColor": "white", "color": None}}):
    import pandas
    import dash, dash_table
    path = "C:/Users/Usuario/Documents/module_approach/liquepedia/top_players_{}.csv".format(game)
    df1 = pandas.read_csv(path).iloc[:5]
    df2 = pandas.DataFrame(["1°", "2°", "3°", "4°", "5°"], columns = ["Posição"])
    df = pandas.concat([df1, df2], axis = 1)
    data = df.to_dict("records")
    table = dash_table.DataTable(
        id = "top_players_table_object",
        data = data,
        columns = [{"id": df.columns[0], "name": "Nome"}, {"id": df.columns[1], "name": "Posição"}],
        style_table = {"width": 450, "height": 400},
        style_header = {"height": 40, "backgroundColor": color_settings["style_header"]["backgroundColor"]},
        style_data = {"height": 35},
        style_cell = {"textAlign": "left", "backgroundColor": color_settings["style_cell"]["backgroundColor"], "color": color_settings["style_cell"]["color"]},
        fill_width = True
    )
    return table

table = create_table_("lol")