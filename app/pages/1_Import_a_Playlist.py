import streamlit as st
import spotipy
from spotipy import SpotifyClientCredentials
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
#export SPOTIPY_CLIENT_ID = ''
#export SPOTIPY_CLIENT_SECRET = ''


client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15)
