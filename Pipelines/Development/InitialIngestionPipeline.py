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


# establish connection to Spotify API

cid = 'b1d63d0b2fcc4b379cf7b7ad0d9d9fc0'
secret = '87f181a928e04a40977a281e9900e3b9'
client_credentials = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15, retries=10)

# establish connection to Postgres

host_name = 'localhost'
database_name = 'Spotify'
engine = sql.create_engine('postgresql+psycopg2://postgres:DataNerd2023!!\
@localhost/Spotify')

# load training data
new_batch = pd.read_csv('distinct_playlists.csv')[['playlist_uri', 'playlist_name']]
new_batch['playlist_uri'] = new_batch['playlist_uri'].str.strip()

db_query = pd.read_sql('SELECT DISTINCT playlist_uri FROM playlist_tracks', engine)

outer = new_batch.merge(db_query, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)

new_batch = pd.DataFrame(anti_join)
new_batch = new_batch[0:25]


load_batch = []
series = new_batch['playlist_uri'].to_dict()
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
                tracks = tracks.rename(columns={"name":"playlist_name", "track.name":"track_name", "track.uri":"track_uri", "track.album.name":"album_name", "track.explicit":"isExplicit", "track.album.release_date":"release_date", "track.duration_ms":"duration_ms", "track.album.uri":"album_uri", "added_by.external_urls.spotify": "added_by_external_urls_spotify", 'added_by.href':"added_by_href", "added_by.id":"added_by_id", "added_by.type":"added_by_type", "added_by.uri":"added_by_uri", "track.album.album_type":"track_album_album_type", "track.album.external_urls.spotify":"track_album_external_urls_spotify", "track.album.href":"track_album_href", "track.album.id":"track_album_id", "track.album.release_date_precision":"track_album_release_date_precision", "track.album.total_tracks":"track_album_total_tracks","track.album.type":"track_album_type", "track.disc_number":"track_disc_number", "track.episode":"track_episode", "track.external_ids.isrc":"track_external_ids_isrc", "track.external_urls.spotify":"track_external_ids_spotify", "track.href":"track_href", "track.id":"track_id", "track.is_local":"track_is_local", "track.popularity":"track_popularity", "track.preview_url":"track_preview_url", "track.track":"track_track", "track.track_number":"track_track_number", "track.type":"track_type", "video_thumbnail.url":"video_thumbnail_url", "external_urls.spotify":"external_urls_spotify", "followers.href":"followers_href", "followers.total":"followers_total", "owner.display_name":"owner_display_name", "owner.external_urls.spotify":"owner_external_urls_spotify", "owner.href":"owner_href", "owner.id":"owner_id", "owner.type":"owner_type", "owner.uri":"owner_uri", "tracks.href":"tracks_href", "tracks.limit":"tracks_limit", "tracks.next":"tracks_next", "tracks.offset":"tracks_offset", "tracks.previous":"tracks_previous", "tracks.total":"tracks_total"})
                tracks = tracks.drop(columns=['track.album.artists', 'track.album.available_markets', 'track.album.images', 'track.artists', 'track.available_markets', 'images', 'tracks.items'])

                load_batch.append(tracks)
        else:
                secondary_data = pd.json_normalize(sp.playlist(playlist))
                tracks['playlist_uri'] = playlist
                tracks = tracks.merge(secondary_data, left_on='playlist_uri', right_on='uri')
                tracks = tracks.rename(columns={"name":"playlist_name", "track.name":"track_name", "track.uri":"track_uri", "track.album.name":"album_name", "track.explicit":"isExplicit", "track.album.release_date":"release_date", "track.duration_ms":"duration_ms", "track.album.uri":"album_uri", "added_by.external_urls.spotify": "added_by_external_urls_spotify", 'added_by.href':"added_by_href", "added_by.id":"added_by_id", "added_by.type":"added_by_type", "added_by.uri":"added_by_uri", "track.album.album_type":"track_album_album_type", "track.album.external_urls.spotify":"track_album_external_urls_spotify", "track.album.href":"track_album_href", "track.album.id":"track_album_id", "track.album.release_date_precision":"track_album_release_date_precision", "track.album.total_tracks":"track_album_total_tracks","track.album.type":"track_album_type", "track.disc_number":"track_disc_number", "track.episode":"track_episode", "track.external_ids.isrc":"track_external_ids_isrc", "track.external_urls.spotify":"track_external_ids_spotify", "track.href":"track_href", "track.id":"track_id", "track.is_local":"track_is_local", "track.popularity":"track_popularity", "track.preview_url":"track_preview_url", "track.track":"track_track", "track.track_number":"track_track_number", "track.type":"track_type", "video_thumbnail.url":"video_thumbnail_url", "external_urls.spotify":"external_urls_spotify", "followers.href":"followers_href", "followers.total":"followers_total", "owner.display_name":"owner_display_name", "owner.external_urls.spotify":"owner_external_urls_spotify", "owner.href":"owner_href", "owner.id":"owner_id", "owner.type":"owner_type", "owner.uri":"owner_uri", "tracks.href":"tracks_href", "tracks.limit":"tracks_limit", "tracks.next":"tracks_next", "tracks.offset":"tracks_offset", "tracks.previous":"tracks_previous", "tracks.total":"tracks_total"})
                tracks = tracks.drop(columns=['track.album.artists', 'track.album.available_markets', 'track.album.images', 'track.artists', 'track.available_markets', 'images', 'tracks.items'])
                load_batch.append(tracks)
    except:
            pass
load_batch = pd.concat(load_batch)
load_batch.to_sql('playlist_tracks', engine, if_exists='append')

df = pd.read_sql('''SELECT DISTINCT track_uri FROM playlist_tracks ORDER BY track_uri''', engine)

outer = df.merge(load_batch, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)

df = pd.Series(anti_join['track_uri'].head(100))
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

df2['RN'] = df2.groupby("track_uri")["name"].rank(method="first", ascending=True)
df2

df2 = df2.pivot(index='track_uri', columns=['RN'], values='name').reset_index()
df2 = df2.rename(columns={1.0:'artist1', 2.0:'artist2', 3.0:'artist3', 4.0:'artist4', 5.0:'artist5'})
df2 = df2[['track_uri', 'artist1', 'artist2', 'artist3', 'artist4', 'artist5']]

df2.to_sql('artists', con=engine, if_exists='append')


df = pd.read_sql('''SELECT DISTINCT track_uri FROM playlist_tracks''', engine)
outer = df.merge(load_batch, how='outer', indicator=True)
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)
df = pd.Series(anti_join['track_uri'])

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
