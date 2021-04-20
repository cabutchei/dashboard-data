import pandas

df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/steam_data/top_games_by_ccu - Copy.csv")

def plot_data(games, date):
    boolean = [x[:10] == date for x in df.Hora] #lista de booleano usado para filtrar o df pela data
    results_by_date = df[boolean]
    results_by_date.reset_index(drop = True, inplace = True) #resetando os indexes

    for i in range(len(results_by_date)):
        hours = int(results_by_date.Hora[i][-5: -3]) #hora em inteiro(horas e minutos são extraídos por string slicing)
        minutes = int(results_by_date.Hora[i][-2:]) #análogo
        minutes_in_hours = round(minutes/60, 3) #convertendo os minutos em horas e arredondando para 3 casas decimais
        results_by_date.Hora[i] = hours + minutes_in_hours
        
    results_by_date_and_name = [] #lista de dataframes, cada elemento é um dataframe relativo a um dos jogos
    for game in games:
        data = results_by_date.loc[lambda x : x.Nome == game]
        results_by_date_and_name.append(data)

    return pandas.concat(results_by_date_and_name)





