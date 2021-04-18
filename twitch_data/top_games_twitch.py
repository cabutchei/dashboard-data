import pandas

file_path = "C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_from_past_week.csv"
df = pandas.read_csv(file_path)
number_of_entries = len(df["Nome"])

if number_of_entries % 8 == 0:
    ranking = []  #lista de listas, o índice de cada sublista representa uma posição no ranking e seus elementos são dicionários
                  #a n-ésima sublista contém todas as entradas para a n-ésima posição de cada request feita 
    all_games = [] #lista com todos os nomes de todos os jogos(sem repetições) 
    data = {} #dicionário principal, contém todos os jogos que apareceram no documento e suas estatísticas relevantes
    for i in range(8):
        number_of_groups = number_of_entries // 8 #grupo corresponde a um request(um top 8)
        place = [] #place representa cada sublista que será adicionada à lista ranking
        for j in range(number_of_groups):
            index = 8 *  j + i #index é o índice no dataframe de cada posição i+1 avaliada(onde i = index(mod 8)) 
            place.append(dict(Nome = df["Nome"][index], Visualizações = df["Visualizações"][index], Canais = df["Canais"][index]))
        for game in place: 
            if game["Nome"] not in all_games: #garante a unicidade de cada nome em all_games
                all_games.append(game["Nome"])
        ranking.append(place)
    
    for game in all_games:
        data[game] = {} #cada loop cria uma nova chave dentro de data(para cada jogo) cujos valores são as estatísticas
        names_top_1 = list(map(lambda x : x["Nome"], ranking[0]))
        top_3 = ranking[0] + ranking[1] + ranking[2] 
        names_top_3 = list(map(lambda x : x["Nome"], top_3))
        views = []
        denominator = 0 #representa o número de vezes que o jogo avaliado constou no documento(em qualquer posição)
        for rank in ranking:
            for jogo in rank: #iterando sobre cada jogo em cada posição
                if jogo["Nome"] == game:
                    views.append(jogo["Visualizações"])
                    denominator += 1
        data[game]["Top 1"] = names_top_1.count(game)
        freq1 = data[game]["Top 1"] / number_of_groups * 100 #<--atualização 
        data[game]["Frequência no Top 1"] = "%.2f" % freq1 + "%" 
        data[game]["Top 3"] = names_top_3.count(game)
        freq3 = data[game]["Top 3"] / number_of_groups * 100 #<--atualização
        data[game]["Frequência no Top 3"] = "%.2f" % freq3 + "%" 
        data[game]["Top 8"] = denominator
        freq8 = data[game]["Top 8"] / number_of_groups * 100
        data[game]["Frequência no Top 8"] = "%.2f" % freq8 + "%" 
        average_views = int(round(sum(views)/denominator)) #arredonda a soma da lista views e converte em int
        data[game]["Visualização Média"] = average_views
        peak_views = max(views)
        data[game]["Pico de Visualizações"] = peak_views


    rows = [[game] + list(data[game].values()) for game in data] #somei cada game(i.e a chave de cada dic) com seus valores em uma só lista
    #o resultado é uma lista de listas, onde cada lista corresponde a uma linha do dataframe
    columns = ["Nome", "Top 1", "Frequência no Top 1", "Top 3", "Frequência no Top 3", "Top 8", "Frequência no Top 8", "Visualização Média", "Pico de Visualizações"]
    rows.sort(reverse = True, key = lambda item : float(item[4][:-1])) #key define o critério de ordenamento
    #o critério definido foi a frequência no top 3
    df2 = pandas.DataFrame(rows, columns = columns)
    print(df2)
    #df2.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv", index = False, encoding="utf-8-sig")
