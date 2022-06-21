import time
from time import sleep
import csv
from csv import reader
from random import randint
import pandas
import pandas as pd
from pandas import DataFrame
from pytube import Playlist

input_filename = 'gatesmashersurls.csv'
with open(input_filename, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:

        url = str(row[0])
        p = Playlist(url)

        for video in p.videos:
            playlist_stats = []

            playlist_stats.append(p.title)
            playlist_stats.append(url)
            playlist_stats.append(len(p.video_urls))
            playlist_stats.append(video.title)
            playlist_stats.append(video.views)
            playlist_stats.append(video.publish_date)
            playlist_stats.append(video.length)
            playlist_stats.append(video.author)
            playlist_stats.append(video.keywords)
            playlist_stats.append(video.video_id)
            playlist_stats.append(video.captions)
            # video.streams.first().download()
            with open(r'playlist_stats.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(playlist_stats)
stats = pd.read_csv("playlist_stats.csv")
header = ["playlist_title","url","count","video_title","views","publish_date","video_length","author","keywords","video_id","video_captions"]
stats.to_csv("stats.csv",header=header)
