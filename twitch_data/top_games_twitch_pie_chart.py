import pandas
import plotly.express as px

df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv").filter(items = ["Nome", "Top 1"])
df = df[lambda x : x["Top 1"] > 0]
fig = px.pie(df, values = "Top 1", names = "Nome")
fig.update_layout(title = "Top jogos da Twitch por frequência no primeiro lugar")
fig.show()