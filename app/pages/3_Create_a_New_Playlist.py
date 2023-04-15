import streamlit as st
from st_aggrid import *
import pandas as pd
import plotly.express as px
import plotly as pl

st.set_page_config(page_title="Create a Playlist", page_icon="📈")

#Windows Environment
#$Env:SPOTIPY_CLIENT_ID = ''
#$Env:SPOTIPY_CLIENT_SECRET = ''
#
#linux/docker
#export SPOTIPY_CLIENT_ID = ''
#export SPOTIPY_CLIENT_SECRET = ''

#Windows Environment
#$Env:SPOTIPY_CLIENT_ID = ''
#$Env:SPOTIPY_CLIENT_SECRET = ''
#
#linux/docker
#export SPOTIPY_CLIENT_ID = ''
#export SPOTIPY_CLIENT_SECRET = ''


# client_id = os.getenv('SPOTIPY_CLIENT_ID')
# client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15)

# client_id = os.getenv('SPOTIPY_CLIENT_ID')
# client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15)

st.title("Create a New Playlist")
st.header("How to create a playlist")
st.write("FIXME - add instructions")

st.header("Choose songs for playlist")
choose_songs_box = pd.DataFrame(columns=["Track", "Artist", "Album", "Length"])
st.dataframe(choose_songs_box)

st.header("Chosen playlist")
temp_dataframe = pd.DataFrame(columns=["Track", "Artist", "Album", "Length"])
st.dataframe(temp_dataframe)

st.button('Generate Playlist')

temp_song_metrics = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['danceability','tempo','runtime',
           'genre', 'beat']))
fig = px.bar_polar(temp_song_metrics, r='r', theta='theta')
st.plotly_chart(fig)


avg_bpm, avg_track_dur, total_dur = st.columns(3)
with avg_bpm:
   st.metric(label="Average BPM", value="180 BPM")

with avg_track_dur:
   st.metric(label="Average Track Duration", value="3:45")

with total_dur:
   st.metric(label="Total Duration", value="1:12:36")

st.header("AI Recommended Songs")

temp_rec_songs = pd.DataFrame(columns=["Track", "Artist", "Album", "Length"])
st.dataframe(temp_dataframe)

st.button('Reset Playlist')



