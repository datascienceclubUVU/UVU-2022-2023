import streamlit as st
from st_aggrid import *
import pandas as pd
import plotly.express as px
import plotly as pl

# Page configuration.
st.set_page_config(
    page_title="Select Preloaded Playlist",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"About": "https://github.com/datascienceclubUVU/UVU-2022-2023"}
)

# Page title.
st.title("Select Preloaded Playlist")

st.markdown("---")

# Instructions for selecting a preloaded playlist.
st.header("How to select a preloaded playlist:")

st.markdown(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eu consectetur leo.
    Vestibulum egestas leo in viverra lobortis. Quisque consectetur viverra libero
    vitae vestibulum. Nulla interdum aliquet lorem. In facilisis orci nec venenatis
    lacinia. Vivamus lorem neque, maximus at pretium nec, fringilla quis mauris. In
    fringilla, nulla in eleifend tempor, mi massa suscipit magna, a varius dolor diam
    nec velit. Mauris ut laoreet diam.
    """
)

st.markdown("---")

# "Select Playlist" dropdown.
st.header("Select Playlist")

preloaded_playlist = st.selectbox(
    label="Preloaded Playlists:",
    options=["Fake Playlist", "Real Playlist", "Imaginary Playlist"],
    help=(
        """
        This dropdown contains preloaded playlists that are used to generate AI
        recommended songs based on the selected playlist.
        """
    )
)

# Grab selected playlist's data.
temp_dataframe = pd.DataFrame(
    columns=[
        "Track",
        "Artist",
        "Album",
        "Length",
        "Tempo",
        "Danceability",
        "Valence",
        "Mood",
        "Beat",
        "Key",
        "Time Signature"
    ]
)

# Display selected playlist's data.
grid_options = GridOptionsBuilder.from_dataframe(temp_dataframe)
grid_options.configure_pagination(paginationAutoPageSize=False, paginationPageSize=10)
grid_options.configure_side_bar()

AgGrid(temp_dataframe, gridOptions=grid_options.build(), reload_data=True, key=0)

# Grab selected playlist's metrics.
temp_playlist_metrics = pd.DataFrame(
    dict(
        r=[1, 5, 2, 2, 3],
        theta=['danceability', 'tempo', 'runtime', 'genre', 'beat']
    )
)

# Display selected playlist's polar chart.
polar_fig = px.bar_polar(temp_playlist_metrics, r='r', theta='theta')

st.plotly_chart(polar_fig)

# Display selected playlist's metrics.
avg_bpm, avg_track_dur, total_dur = st.columns(3)
with avg_bpm:
   st.metric(label="Average BPM", value="180 BPM")
with avg_track_dur:
   st.metric(label="Average Track Duration", value="3:45")
with total_dur:
   st.metric(label="Total Duration", value="1:12:36")

# "Generate AI Recommended Songs" button.
st.button(
    label="**Generate AI Recommended Songs**",
    help=(
        """
        Generates AI recommended songs based on the currently selected preloaded
        playlist when clicked.
        """
    ),
    type="primary"
)

st.markdown("---")

# Display song recommendations.
st.header("AI Recommended Songs")

# Generate AI recommended songs from the selected preloaded playlist.
temp_dataframe = pd.DataFrame(
    columns=[
        "Track",
        "Artist",
        "Album",
        "Length",
        "Tempo",
        "Danceability",
        "Valence",
        "Mood",
        "Beat",
        "Key",
        "Time Signature"
    ]
)

# Display generated AI song recommendations.
grid_options = GridOptionsBuilder.from_dataframe(temp_dataframe)
grid_options.configure_pagination(paginationAutoPageSize=False, paginationPageSize=10)
grid_options.configure_side_bar()

AgGrid(temp_dataframe, gridOptions=grid_options.build(), reload_data=True, key=1)
