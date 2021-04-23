import pandas, module
import plotly.express as px

# df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv").filter(items = ["Nome", "Top 1"])
df = pandas.read_csv("C:/Users/Usuario/Documents/Visual Studio Code/dashboard/twitch_data/top_games_twitch_stats.csv")
df = module.filter_by_row_and_column(df = df, columns = ["Nome", "Top 1"])
df = module.filter_by_condition(df, "Top 1", lambda x : x > 0)


fig = px.pie(df, values = "Top 1", names = "Nome")
fig.update_layout(title = "Top jogos da Twitch por frequência no primeiro lugar")
fig.show()