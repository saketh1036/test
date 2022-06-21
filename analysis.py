import pandas as pd

data = pd.read_csv("stats.csv")
grouped_data = data.groupby("playlist_title")
stats = []
for title,playlist_data in grouped_data:
    temp_list = []
    temp_list.append(title)
    temp_list.append(playlist_data["views"].sum())
    temp_list.append(playlist_data["views"].mean())
    stats.append(temp_list)
header = ["title","total_views","views_per_video"]
dataframe = pd.DataFrame(stats,columns=header)
dataframe = dataframe.sort_values(by=["views_per_video"])
print(dataframe)
dataframe.to_csv("final_stats.csv")
