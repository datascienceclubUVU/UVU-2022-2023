import streamlit as st
import os

st.set_page_config(page_title="Create a Playlist", page_icon="📈")

st.markdown("# Create a Playlist")
st.sidebar.header("Create a Playlist")
st.write(
    """This demo creates a Playlist"""
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
