import pandas, module
data = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu - Copy.csv")
all_games = module.get_unique_values(data["Nome"])

rows = []
for game in all_games: 
    d = module.filter_by_name(data, "Nome", game)
    total_ccu = sum(d["ccu"])
    occurrences = len(d)
    average_ccu = int(round(total_ccu / occurrences))
    rows.append([game, average_ccu])
rows.sort(reverse = True, key = lambda x : x[1])    
df = pandas.DataFrame(rows, columns = ["Nome", "Média de ccu"])
print(df)
#df.to_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu_stats.csv", index = False, encoding = "utf-8-sig")