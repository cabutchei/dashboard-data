##Esse script organiza em estatística os dados obtidos pelos requests de top_games_by_ccu.py

import pandas
data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu - Copy.csv")
number_of_entries = len(data.Nome)
number_of_groups = number_of_entries // 8
all_entries = list(data.Nome)
all_games = []

def find_all(parameter, iterable): #retorna uma lista com os índices de todas as instâncias de parameter dentro de um iterável
    indexes = []
    i = 0
    for element in iterable:
        if element == parameter:
            indexes.append(i)
        i += 1
    return indexes

for game in data.Nome: #preenche all_games com todos os jogos de maneira única
    if all_games.count(game) == 0:
        all_games.append(game)


rows = []
for game in all_games: 
    total_ccu = 0
    indexes = find_all(game, data.Nome)
    for index in indexes: #iterando sobre a lista retornada por find_all
        total_ccu += data.ccu[index] #atualizando a conta de total_ccu para cada ocorrência(índice)
    occurrences = len(indexes)
    average_ccu = int(round(total_ccu / occurrences))
    rows.append([game, average_ccu])
rows.sort(reverse = True, key = lambda x : x[1])    
df = pandas.DataFrame(rows, columns = ["Nome", "Média de ccu"])
#print(df)
#df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv", index = False, encoding = "utf-8-sig")

