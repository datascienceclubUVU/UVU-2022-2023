import streamlit as st
import spotipy
import pandas as pd
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOauthError, SpotifyStateError, SpotifyException
import re
import os
import math

st.set_page_config(page_title="Import Playlist", page_icon="📈")

st.markdown("# Import Playlist")
st.sidebar.header("Import Playlist")
st.write(
    """This demo Imports a Playlist!"""
)

#Windows Environment
#$Env:SPOTIPY_CLIENT_ID = ''
#$Env:SPOTIPY_CLIENT_SECRET = ''
#
#linux/docker
#export SPOTIPY_CLIENT_ID ''
#export SPOTIPY_CLIENT_SECRET ''
# If necessary, we can also add environment variables in linux like so:
#   vim ~/.bashrc
#   add the following to the end of the file:
#   SPOTIPY_CLIENT_ID=''
#   SPOTIPY_CLIENT_SECRET=''


client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15)


# Idea of this pipeline is to allow a user to paste in the URL for their playlist and extract the playlist URI
# pl = 'https://open.spotify.com/playlist/4xjKk78zyTBjWzGjZ0HfDk?si=239973d3db4d41ce&pt=03042c4e3c2399a6889c1b8573e04052'
# C&C - https://open.spotify.com/playlist/4xjKk78zyTBjWzGjZ0HfDk?si=a3f654b6db204ca6
# T&S - https://open.spotify.com/playlist/44TAn9OTwVDnKNzGY2JxOV?si=f4055168e94a42c7
# Crabs - https://open.spotify.com/playlist/1ZAo2hHlDWcCNNobChKp0D?si=56958c737d694edb
pl = st.text_input(label="Please enter playlist URL:")#,value='https://open.spotify.com/playlist/4xjKk78zyTBjWzGjZ0HfDk?si=a3f654b6db204ca6')
x= re.split('\/|\?',pl)
playlist_id = x[4]

try:
    playlist = sp.playlist(playlist_id=playlist_id)
    while playlist['tracks']['next']:
        results = sp.next(playlist['tracks'])
        playlist['tracks']['items'].extend(results['items'])
        playlist['tracks']['next'] = results['next']
    playlist_image = sp.playlist_cover_image(playlist_id=playlist_id)[0]['url']
    playlist_name = playlist['name']
    playlist_description = ['description']
    tracks = []
    track_uris = []
    for x in playlist['tracks']['items']:
        track_dict = {}
        track_dict['track_name'] = x['track']['name']
        track_dict['artist_name'] = x['track']['artists'][0]['name']
        track_dict['album_name'] = x['track']['album']['name']
        track_dict['release_date'] = release_date = x['track']['album']['release_date']
        track_dict['release_year'] = release_date.split('-')[0]
        track_dict['track_popularity'] = x['track']['popularity']
        track_dict['duration_ms'] = x['track']['duration_ms']
        track_dict['is_explicit'] = x['track']['explicit']
        track_dict['track_uri'] = x['track']['uri']
        tracks.append(track_dict)
        track_uris.append(track_dict['track_uri'])
    audio_features = []
    calls = math.ceil(len(track_uris) / 100)
    for x in range(calls):
        if len(track_uris) > 100:
            uri_sublist = track_uris[:100]
            track_uris = track_uris[100:]
            af_results = sp.audio_features(uri_sublist)
            audio_features.extend(af_results)
        else:
            af_results = sp.audio_features(track_uris)
            audio_features.extend(af_results)
    for track, audio in zip(tracks, audio_features):
        track['danceability'] = audio['danceability']
        track['energy'] = audio['energy']
        track['instrumentalness'] = audio['instrumentalness']
        track['valence'] = audio['valence']
        track['tempo'] = audio['tempo']

    st.image(playlist_image)

except SpotifyException:
    st.write("That playlist does not exist or is private. Try again.")
