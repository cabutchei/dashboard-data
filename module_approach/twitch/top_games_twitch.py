import pandas, module

file_path = "C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_from_past_week.csv"
df = pandas.read_csv(file_path)
number_of_entries = len(df)

if number_of_entries % 8 == 0:
    number_of_groups = number_of_entries // 8 #número de grupos(requests)
    ranking = []  #lista de dataframes, cada dataframe se refere a uma das oito posições do ranking e guarda as informações dos jogos
    all_games = module.get_unique_values(df["Nome"]) #lista com todos os nomes de todos os jogos(sem repetições) 
    for mod in range(8): #mod representa cada resto possível na divisão por 8(0 a 7)
        indexes = [] #todos índices no dataframe geral relativos a cada posição(a posição é definida por mod)  
        for factor in range(number_of_groups):
            indexes.append(8 * factor + mod) 
        place = module.filter_by_row_and_column(df, indexes) #filtrando df usando indexes como filtro
        ranking.append(place)
    
    rows = [] #as linhas do dataframe final de estatísticas(lista de listas)
    for game in all_games:
        all_occurences = module.filter_by_name(df, "Nome", [game])
        number_of_occurrences = len(all_occurences)
        
        top1 = module.count(game, ranking[0]["Nome"])
        freq1 = top1 / number_of_groups * 100
        freq1 = "%.2f" %freq1 + "%"
        
        top3 = module.count(game, ranking[0]["Nome"]) + module.count(game, ranking[1]["Nome"]) + module.count(game, ranking[2]["Nome"])
        freq3 = top3 / number_of_groups * 100
        freq3 = "%.2f" %freq3 + "%"

        top8 = module.count(game, df["Nome"])
        freq8 = top8 / number_of_groups * 100
        freq8 = "%.2f" %freq8 + "%"

        views = 0
        for view in all_occurences["Visualizações"]:
            views += view
        average_views = int(round(views / number_of_occurrences))

        peak_views = max(all_occurences["Visualizações"])
        
        rows.append([game, top1, freq1, top3, freq3, top8, freq8, average_views, peak_views])

    columns = ["Nome", "Top 1", "Frequência no Top 1", "Top 3", "Frequência no Top 3", "Top 8", "Frequência no Top 8", "Visualização Média", "Pico de Visualizações"]
    rows.sort(reverse = True, key = lambda item : float(item[4][:-1]))
    stats_df = pandas.DataFrame(rows, columns = columns)
    stats_df.to_csv("C:/Users/Usuario/Documents/github_temp/twitch/top_games_twitch_stats.csv")