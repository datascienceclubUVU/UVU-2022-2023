'''
Python libraries allow users to extend the abilities of the language compiler. For this project, I will be using the following libraries:
- pandas and numpy (for data analysis and manipulation)
- streamlit and plotly (for UI design and data visualization)
- pyodbc and spotipy (for Spotify API and SQL Server connections)
'''

# import libraries
import plotly
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import sqlalchemy as db
import pyodbc
from random import seed
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# define function to highlight output dataframe cells based on value

def highlight_colors(val, color_if_true, color_if_false):
    color = color_if_true if val >= 0.75 and val <= 1.0 else color_if_false
    return 'background-color: {}'.format(color)

# establish API connection

cid = '3fda75b7146a4769b207ee44017b3abe'
secret = '2a755cb04a18406b9394dbef2f8069dd'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# establish SQL Server connection

engine = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};""Server=192.168.1.132;""Database=Spotify;""Trusted_Connection=yes;")
cursor = engine.cursor()


# create initial query

query = pd.read_sql('''SELECT DISTINCT dt.track_name, dt.artist_name, dt.track_uri, da.artist_uri, af.*
FROM audio_features2 af 
JOIN dim_tracks dt ON af.uri = dt.track_uri2
JOIN dim_artists da ON dt.artist_name = da.artist_name''', connection)

# transform query fields

query['music_key'] = query['music_key'].map({0: 'C', 1: 'C#/Db', 2: 'D', 3: 'D#/Eb', 4: 'E', 5: 'F', 6: 'F#/Gb', 7: 'G', 8: 'G#/Ab', 9: 'A', 10: 'A#/Bb', 11: 'B'})
query['modal'] = query['modal'].map({'0': 'Minor', '1': 'Major'})
query['time_signature'] = query['time_signature'].map({'3': '3/4', '4': '4/4', '5': '5/4', '6': '6/4', '7': '7/4'})

# create metrics for analysis

query2 = pd.melt(query, id_vars=['uri'], var_name='metrics', value_name='score', value_vars=['instrumentalness', 'danceability', 'energy', 'acousticness', 'valence', 'liveness'])



# name the app                  

st.set_page_config(page_title='Song Recommendation App', layout='centered')

# create internal CSS

st.markdown(""" <style> 
                        .title { font-size: 45px;
                                 text-align: center;}
                        .track { font-size: 20px;
                                 text-align: left;
                                 padding-left: 50px;
                                 padding-top: 30px;}
                        .artist { font-size: 15px;
                                  text-align: left;
                                  padding-left: 85px;}
                        .subheader { font-size: 22px;
                                     text-align: left;}
                        .header { font-size: 20px;
                                  padding-left: 35px;
                                  font-weight: bold;}
                        .header2 { font-size: 20px;
                                   padding-left: 33px;
                                   font-weight: bold;}
                        .header3 { font-size: 20px;
                                   padding-left: 25px;
                                   font-weight: bold;}
                        .header4 { font-size: 20px;
                                   padding-left: 0px;
                                   font-weight: bold;}
                        .header5 { font-size: 25px;
                                   padding-left: 225px;
                                   margin-top: 50px;
                                   margin-bottom: 50px;}
                        .ban-font { font-size: 30px;
                                    padding-left: 25px;}
                        .ban-font2 { font-size: 30px;
                                  padding-left: 25px;}
                        .ban-font3 { font-size: 30px;
                                     padding-left: 0px;}
                        .ban-font4 { font-size: 30px;
                                     padding-left: 30px;}
                        .image { padding-top: 10px;}
                        .streamlit-expanderHeader { font-size: 22px;}
                        .row_heading.level0 {display:none}
                        .blank {display:none}
                                  
                </style>""", unsafe_allow_html=True)

# create sidebar menu

sidebar_title = st.sidebar.header('Create Your Custom Playlist')
artists = query['artist_name'].drop_duplicates()
artists = artists.sort_values()
artist_choice = st.sidebar.selectbox('Choose an Artist:', artists)
tracks = query['track_name'].loc[query['artist_name'] == artist_choice].drop_duplicates()
tracks = tracks.sort_values()
track_choice = st.sidebar.selectbox('Choose a Song', tracks)
empty = st.sidebar.text('')
output = query['uri'].loc[(query['track_name'] == track_choice) & (query['artist_name'] == artist_choice)].values
output_bpm = query['tempo'].loc[(query['track_name'] == track_choice) & (query['artist_name'] == artist_choice)].drop_duplicates().values
output_bpm = output_bpm.astype(float)
output_bpm = np.round(output_bpm, decimals=0)
output_bpm = output_bpm.astype(int)
output_key = query['music_key'].loc[(query['track_name'] == track_choice) & (query['artist_name'] == artist_choice)].drop_duplicates().values
output_mode = query['modal'].loc[(query['track_name'] == track_choice) & (query['artist_name'] == artist_choice)].drop_duplicates().values
output_sig = query['time_signature'].loc[(query['track_name'] == track_choice) & (query['artist_name'] == artist_choice)].drop_duplicates().values
uri_output = st.sidebar.selectbox('Select the URI:', options=(output))


viz_query = query2.loc[query2['uri'] == uri_output]

# create title for main interface

page_title = st.markdown(f'''<h1 class="title"">Song Recommendation Engine 2.0</h1>''', unsafe_allow_html=True)

# create dropdown menu for app description

st.markdown('<br>', unsafe_allow_html=True)
with st.expander('Description'):
    st.markdown('''Have you ever wondered how Spotify's Song Recommendation Algorithm works? This app allows you to take a behind-the-scenes look at how Spotify uses your data to recommend songs based on various metrics.''', unsafe_allow_html=True)
    
# allow user to preview song and view album cover

st.markdown('<br><br><h4>Song Preview</h4><br><br>', unsafe_allow_html=True)

img_query = pd.json_normalize(sp.track(uri_output), record_path=['album', ['images']])
img_url = img_query['url'][0] 
audio_query = pd.json_normalize(sp.track(uri_output))
audio_url = audio_query['preview_url'][0]
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    if audio_url != None:
        st.audio(audio_url)
    else:
        st.text('No Audio Available')
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 4, 1])
with col3:
    album_image = st.markdown(f'<img class= "image" src={img_url} width="125" height="125"></img>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<p class="track">{track_choice}</p>\n<p class="artist">{artist_choice}</p>', unsafe_allow_html=True)
    
# create BANs for data visualizations

col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 1, 1])
with col1:
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    filters_txt = st.markdown('<h4>Features</h4><br><br>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    bpm_ban = st.markdown(f'''<p class="header">BPM</p><p class="ban-font">{output_bpm}</p>''', unsafe_allow_html=True)
with col2:
    key_ban = st.markdown(f'''<p class="header2">Key</p><p class="ban-font2">{output_key}</p>''', unsafe_allow_html=True)
with col3:
    mode_ban = st.markdown(f'''<p class="header3">Mode</p><p class="ban-font3">{output_mode}</p>''', unsafe_allow_html=True)
with col4:
    sig_ban = st.markdown(f'''<p class="header4">Time Signature</p><p class="ban-font4">{output_sig}</p>''', unsafe_allow_html=True)

# create data visualization using new query from uri output



fig = px.bar_polar(viz_query, theta='metrics', r='score', range_r=[0.0,1.0], hover_name='metrics', hover_data={'score':True, 'metrics':False}, width=750, height=600, color_continuous_scale='Sunset', color='score', range_color=[0.0,1.0], template='plotly', title='Song Metrics')
fig = fig.update_layout(polar_radialaxis_gridcolor="#e3ecf6", polar_angularaxis_gridcolor="#e3ecf6", polar= dict(radialaxis= dict(showticklabels= False)), hovermode="x")
fig = fig.update_traces(hovertemplate="<b>Metric: %{theta}<br>Score: %{r}</b>", hoverlabel= dict(bgcolor="#ffffff"))
st.plotly_chart(fig)

# create drop-down menu to display definitions for each metric

with st.expander('Metric Definitions'):
    st.markdown(f'''<h4><b><u>Acousticness</u></b></h4>\nA confidence measure from 0.00 to 1.00 of whether a track is acoustic. 1.0 represents high confidence the track is acoustic.\n\n<h4><b><u>Danceability</u></b></h4>\nThis describes how suitable a track is for dancing based on a combination of musical elements including tempo (BPM), rhythm stability, beat strength, and overall regularity. A value of 0.00 is least danceable and 1.00 is most danceable.\n\n<h4><b><u>Energy</u></b></h4>\nA measure from 0.00 to 1.00 that represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.\n\n<h4><b><u>Instrumentalness</u></b></h4>\nPredicts whether a tracks contains no vocals. "Ooh" and "Aah" sounds are treated as instrumental in this context. The closer the value is to 1.00, the greater likelihood the track contains no vocal content.\n\n<h4><b><u>Liveness</u></b></h4>\nDetects the presence of an audience in the recoding. The great the value is to 1.00, the greater the likelihood that the track was performed live.\n\n<h4><b><u>Valence</u></b></h4>\nA measure from 0.00 to 1.00 describing the musical positiveness by a track. Tracks with high valence (> 0.50) sound more positive, whereas tracks with low valence (< 0.50) sound more negative.\n\n<br><i>* Web API Reference: Get Track Audio Features, Spotify, developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features.</i>''', unsafe_allow_html=True)
    
# create drop-down menu to display song recommendations based on user input

with st.expander('Song Recommendations'):
    st.subheader('Your Song')
    result_query = pd.read_sql(f'''SELECT dt.track_name, dt.album_name, da.artist_uri, da.artist_name, af.* 
                               FROM audio_features2 af 
                               JOIN dim_tracks dt ON dt.track_uri2 = af.uri 
                               JOIN dim_artists da ON da.artist_name = dt.artist_name 
                               WHERE dt.track_uri2 = ?''', engine, params=[uri_output])
    result_query = result_query.drop_duplicates()
    result_df = pd.DataFrame(result_query)
    result_df = result_df[['track_name', 'artist_name', 'album_name', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence', 'artist_uri', 'uri']]
    if len(result_df) > 1:
        viz_query['metrics'] = viz_query['metrics']/len(result_df)
        st.dataframe(result_df)
    else:
        st.dataframe(result_df)
    
    
    # get all artist data
    
    result_list2 = pd.json_normalize(sp.recommendations(seed_tracks=[result_df['uri'][0]], seed_artists=[result_df['artist_uri'][0]], limit=25), record_path=['tracks', ['artists']])
    
    # create output dataframe for song recommendations
    
    result_list2 = result_list2.merge(query, left_on='uri', right_on='artist_uri')
    result_list2 = result_list2.rename(columns={'name': 'Artist Name', 'uri_x': 'Artist URI'})
    result_list2 = result_list2.rename(columns={'track_name': 'Track Name'})
    final_df = result_list2[['Track Name', 'Artist Name', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence']].head(25)
    
    # create new field to calculate likeness for song metrics
    
    for row in final_df:
        if result_df['acousticness'] > final_df['acousticness']:
            likeness1 = (final_df['acousticness']/result_df['acousticness'])
        else:
            likeness1 = (result_df['acousticness']/final_df['acousticness'])
        
        if result_df['danceability'] > final_df['danceability']:
            likeness2 = (final_df['danceability']/result_df['danceability'])
        else:
            likeness2 = (result_df['danceability']/final_df['danceability'])
        
        if result_df['energy'] > final_df['energy']:
            likeness3 = (final_df['energy']/result_df['energy'])
        else:
            likeness3 = (result_df['energy']/final_df['energy'])
        
        if result_df['instrumentalness'] > final_df['instrumentalness']:
            likeness4 = (final_df['instrumentalness']/result_df['instrumentalness'])
        else:
            likeness4 = (result_df['instrumentalness']/final_df['instrumentalness'])
            
        if result_df['liveness'] > final_df['liveness']:
            likeness5 = (final_df['liveness']/result_df['liveness'])
        else:
            likeness5 = (result_df['liveness']/final_df['liveness'])
            
        if result_df['valence'] > final_df['valence']:
            likeness6 = (final_df['valence']/result_df['valence'])
        else:
            likeness6 = (result_df['valence']/final_df['valence'])
        
        likeness_metrics = [likeness1, likeness2, likeness3, likeness4, likeness5, likeness6]
        likeness_metrics = sum(likeness_metrics)/6
        final_df['likeness'] = likeness_metrics
    final_df['acousticness'] = round(final_df['acousticness'].astype(float), 3)
    final_df['danceability'] = round(final_df['danceability'].astype(float), 3)
    final_df['energy'] = round(final_df['energy'].astype(float), 3)
    final_df['instrumentalness'] = round(final_df['instrumentalness'].astype(float), 3)
    final_df['liveness'] = round(final_df['liveness'].astype(float), 3)
    final_df['valence'] = round(final_df['valence'].astype(float), 3)
    final_df = final_df[['Track Name', 'Artist Name', 'likeness', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence']]
    final_df = final_df.drop_duplicates()
    final_df = final_df.sort_values(by=['likeness'], ascending=False)
    final_df = final_df.reset_index()
    final_df = final_df.style.applymap(highlight_colors, color_if_true='#5EFF33', color_if_false='white', subset=['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence'])
    st.subheader('Recommendations (by likeness)')
    st.dataframe(final_df)


    

    
