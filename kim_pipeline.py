# Import all connection libraries

from spotipy import SpotifyClientCredentials
import spotipy
import sqlalchemy as sql
import psycopg2

# Import all data manipulation libraries

import pandas as pd
from pandarallel import pandarallel
import numpy as np
from tqdm import tqdm
pandarallel.initialize(verbose=0, nb_workers=8)

from functools import lru_cache

# Use the lru_cache decorator to cache the result of the function
# maxsize=1000 means the cache will store the result of up to 1000 items
@lru_cache(maxsize=1000)
def get_playlist_tracks(playlist_uri):
    """
    This function uses the Spotify API to get the tracks of a given playlist.
    The function is decorated with the lru_cache decorator to cache the result for each unique playlist_uri.
    So, if the same playlist_uri is passed to the function again, the cached result will be returned
    instead of making a new API call.
    :param playlist_uri: The Spotify URI of the playlist
    :return: A DataFrame containing the tracks of the playlist
    """
    # Use the Spotify API to get the tracks of the playlist
    tracks = pd.json_normalize(sp.playlist_tracks(playlist_uri), record_path=['items'])
    return tracks


cid = 'e5448a8a4fdc4b5d98b44e956d50546d'
secret = '8924c0394d3f49a4a569fc03e891aa1b'
client_credentials = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15, retries=10)

# establish connection to Postgres

host_name = 'localhost'
database_name = 'Spotify'
engine = sql.create_engine('postgresql+psycopg2://postgres:DataNerd2023!!\
@localhost/Spotify')

# load training data
data = pd.read_csv('distinct_playlists.csv')[['playlist_uri', 'playlist_name']]
data['playlist_uri'] = data['playlist_uri'].str.strip()

data2 = pd.read_sql('SELECT DISTINCT playlist_uri FROM playlist_tracks', engine)

outer = data.merge(data2, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)

data = pd.DataFrame(anti_join)
data = data[0:50]

test_list = []
series = data['playlist_uri'].to_dict()
for playlist in tqdm(series.values()):
    try:
        tracks = get_playlist_tracks(playlist)
        if len(tracks) >= 100:
                tracks2 = pd.json_normalize(sp.playlist_tracks(playlist, offset=100), record_path=['items'])
                tracks3 = pd.json_normalize(sp.playlist_tracks(playlist, offset=200), record_path=['items'])
                tracks = pd.concat([tracks, tracks2, tracks3])
                secondary_data = pd.json_normalize(sp.playlist(playlist))
                tracks['playlist_uri'] = playlist
                tracks = tracks.merge(secondary_data, left_on='playlist_uri', right_on='uri')
                tracks = tracks.rename(columns={"name":"playlist_name", "track.name":"track_name", "track.uri":"track_uri", "track.album.name":"album_name", "track.explicit":"isExplicit", "track.album.release_date":"release_date", "track.duration_ms":"duration_ms", "track.album.uri":"album_uri"})
                tracks = tracks.drop(columns=['track.album.artists', 'track.album.available_markets', 'track.album.images', 'track.artists', 'track.available_markets', 'images', 'tracks.items'])

                test_list.append(tracks)
        else:
                secondary_data = pd.json_normalize(sp.playlist(playlist))
                tracks['playlist_uri'] = playlist
                tracks = tracks.merge(secondary_data, left_on='playlist_uri', right_on='uri')
                tracks = tracks.rename(columns={"name":"playlist_name", "track.name":"track_name", "track.uri":"track_uri", "track.album.name":"album_name", "track.explicit":"isExplicit", "track.album.release_date":"release_date", "track.duration_ms":"duration_ms", "track.album.uri":"album_uri"})
                tracks = tracks.drop(columns=['track.album.artists', 'track.album.available_markets', 'track.album.images', 'track.artists', 'track.available_markets', 'images', 'tracks.items'])
                test_list.append(tracks)
    except:
            pass
test_list = pd.concat(test_list)
test_list.to_sql('playlist_tracks', engine, if_exists='append')

tracks_df = pd.read_sql('''SELECT DISTINCT track_uri FROM playlist_tracks ORDER BY track_uri''', engine)
outer = tracks_df.merge(test_list, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)
df = pd.DataFrame(anti_join)
df = pd.Series(df['track_uri'])
base_list = []
for track in tqdm(df):
    try:
        df2 = pd.json_normalize(sp.track(track), record_path=['artists'])
        df2['track_uri'] = track
        df2 = df2[['name', 'track_uri']]
        base_list.append(df2)
    except:
        pass
df2 = pd.concat(base_list)


tracks_df = pd.read_sql('''SELECT DISTINCT track_uri FROM playlist_tracks ORDER BY track_uri''', engine)
outer = tracks_df.merge(test_list, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)
df = pd.DataFrame(anti_join)
df = pd.Series(df['track_uri'])
base_list = []
for track in tqdm(df):
    try:
        df3 = pd.json_normalize(sp.audio_features(track))
        df3['track_uri'] = track
        df3 = df3[['track_uri', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']]
        base_list.append(df3)
    except:
        pass
df3 = pd.concat(base_list)