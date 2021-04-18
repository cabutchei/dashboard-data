import plotly.express as px
import pandas
game = "pubg"
path = "C:/Users/Usuario/Documents/Visual Studio Code/dashboard/game_popularity/popularity_en/{}.csv".format(game)
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
fig.show()
