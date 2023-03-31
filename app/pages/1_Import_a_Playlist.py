import streamlit as st
import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOauthError, SpotifyStateError, SpotifyException
import re
import os

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
pl = 'https://open.spotify.com/playlist/4xjKk78zyTBjWzGjZ0HfDk?si=239973d3db4d41ce&pt=03042c4e3c2399a6889c1b8573e04052'
x= re.split('\/|\?',pl)
playlist_id = x[4]

try:
    playlist = sp.playlist(playlist_id=playlist_id)
    print(playlist)
except SpotifyException:
    print("That playlist does not exist or is private. Try again.")
