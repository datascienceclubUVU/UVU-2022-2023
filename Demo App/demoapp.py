# import all required libraries

import streamlit as st
import pandas as pd
import spotipy
from spotipy import SpotifyClientCredentials
import numpy as np
import plotly.express as px
from st_aggrid import *

# establish connection with Spotify API

cid = '3fda75b7146a4769b207ee44017b3abe'
secret = '2a755cb04a18406b9394dbef2f8069dd'
client_credentials = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials, requests_timeout=15)

source_data = pd.read_parquet("demodata.parquet.gzip")
source_data['tempo'] = source_data['tempo'].replace(999, 0)
source_data['danceability'] = source_data['danceability'].replace(999,0)
source_data['energy'] = source_data['energy'].replace(999,0)
source_data['instrumentalness'] = source_data['instrumentalness'].replace(999,0)
source_data['liveness'] = source_data['liveness'].replace(999,0)
source_data['valence'] = source_data['valence'].replace(999,0)
source_data['acousticness'] = source_data['acousticness'].replace(999,0)

# configure page layout

st.set_page_config(page_title="Playlist Recommendation App", layout="wide")

# create introduction prompt

header = st.markdown(''' 
            <h2 style="text-align:center">Welcome to the Playlist Song Recommendation App!</h2><br>
            <p style="font-size:20px;text-align:center;">How would you like to access your playlist?</p><br><br>
            ''',unsafe_allow_html=True)

# create selection menu
with st.expander("Import Playlist"):
    
    # retrieve user input
    
    input_box = st.text_input(label="Enter Playlist URI:", value="spotify:playlist:37i9dQZF1DX1nSIVoqxfC0")
    if input_box:
        
        # return user input
        
        source_query = pd.json_normalize(sp.playlist_tracks(input_box), record_path=['items'])
        join_query = pd.json_normalize(sp.playlist(input_box))
        source_query = source_query.rename(columns={'track.name':'track_name', 'track.album.name':'album_name', 'track.explicit':'isExplicit', 'track.album.release_date':'release_date', 'track.duration_ms':'duration_ms', 'track.uri':'track_uri'})
        source_query['playlist_uri'] = input_box
        result_df = source_query[['track_name', 'album_name', 'isExplicit', 'release_date', 'duration_ms', 'track_uri', 'playlist_uri']]
        result_df= result_df.loc[result_df['playlist_uri'] == input_box]
        result_df = result_df[['track_name', 'album_name', 'isExplicit', 'release_date', 'duration_ms']]
        playlist_name = sp.playlist(input_box)['name']
        st.metric(label='Playlist Name', value=playlist_name)
        st.dataframe(result_df)
        
        # display playlist metrics
        
        st.markdown('<h3>Playlist Metrics</h3>', unsafe_allow_html=True)
        source_query = pd.json_normalize(sp.playlist_tracks(input_box), record_path=['items'])
        join_query = pd.json_normalize(sp.playlist(input_box))
        source_query = source_query.rename(columns={'track.name':'track_name', 'track.album.name':'album_name', 'track.explicit':'isExplicit', 'track.album.release_date':'release_date', 'track.duration_ms':'duration_ms', 'track.uri':'track_uri'})
        source_query['playlist_uri'] = input_box
        base_list = []
        tracks = source_query['track_uri'].drop_duplicates()
        for track in tracks:
            features = pd.json_normalize(sp.audio_features(track))
            features = features[['uri','danceability', 'energy', 'instrumentalness', 'acousticness', 'liveness', 'valence', 'tempo']]
            base_list.append(features)
        metrics_query = pd.concat(base_list)
        metrics_query = metrics_query.merge(source_query, left_on='uri', right_on='track_uri')
        metrics_query2 = metrics_query.melt(id_vars=['track_name', 'album_name', 'isExplicit', 'duration_ms', 'release_date'], var_name='metrics', value_name='score', value_vars=['danceability', 'energy', 'instrumentalness', 'acousticness', 'liveness', 'valence'])
        metrics_query2 = metrics_query2.groupby(['metrics'])['score'].mean()
        metrics_query2 = pd.DataFrame(metrics_query2).reset_index()
        fig = px.bar_polar(metrics_query2, theta='metrics', r='score', range_r=[0.0,1.0], hover_name='metrics', hover_data={'score':True, 'metrics':False}, width=750, height=650, color_continuous_scale='Sunset', color='score', range_color=[0.0,1.0], template='plotly')
        fig = fig.update_layout(polar_radialaxis_gridcolor="#e3ecf6", polar_angularaxis_gridcolor="#e3ecf6", polar= dict(radialaxis= dict(showticklabels= False)), hovermode="x")
        fig = fig.update_traces(hovertemplate="<b>Metric: %{theta}<br>Score: %{r}</b>", hoverlabel= dict(bgcolor="#ffffff"))
        metric_chart = st.plotly_chart(fig)
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        with col2:
            bpm_query = metrics_query.loc[metrics_query['playlist_uri'] == input_box]
            output_bpm = bpm_query.groupby('playlist_uri')['tempo'].mean()
            output_bpm = output_bpm.astype(int)
            st.metric(label='Avg. BPM', value=output_bpm)
        with col3:
            duration_query = metrics_query.loc[metrics_query['playlist_uri'] == input_box]
            output_duration = duration_query.groupby('playlist_uri')['duration_ms'].mean()
            output_duration = output_duration/60000
            output_duration = round(output_duration, 2)
            st.metric(label='Avg. Track Duration (Mins)', value=output_duration)
        with col4:
            duration_query1 = metrics_query.loc[metrics_query['playlist_uri'] == input_box]
            output_duration2 = duration_query1.groupby('playlist_uri')['duration_ms'].sum()
            output_duration2 = output_duration2/60000
            output_duration2 = round(output_duration2, 2)
            st.metric(label='Total Duration (Mins)', value=output_duration2)
        
        # compute song recommendations
        
        recommendations = pd.json_normalize(sp.recommendations(seed_tracks=['spotify:track:4r8lRYnoOGdEi6YyI5OC1o'], seed_artists=['spotify:artist:6Ff53KvcvAj5U7Z1vojB5o'], limit=100, seed_genres=sp.recommendation_genre_seeds()), record_path=['tracks'])
    
        # return song recommendations
    
        recommendations = recommendations[['name', 'album.name', 'album.release_date']]
        st.markdown('<h3>Song Recommendations</h3>', unsafe_allow_html=True)
        recommendations_df = st.write(recommendations)

with st.expander('Choose Playlist'):
    options = source_data.sort_values(by=['playlist_name'])
    options = options['playlist_name']
    options = options.loc[options != ''].drop_duplicates()
    options_series = pd.Series(options)
    options_lst = options_series.tolist()
    option_list = st.selectbox(label="Choose A Playlist Below:", options=[x for x in options_lst])

    
    choice_query = source_data.loc[source_data['playlist_name'] == option_list]
    result_query = choice_query[['track_name', 'album_name', 'isExplicit', 'release_date', 'duration_ms', 'track_uri', 'album_uri']]
    gd = GridOptionsBuilder.from_dataframe(result_query)
    gd.configure_pagination(paginationAutoPageSize=False, paginationPageSize=10)
    gd.configure_side_bar()
    final_query = AgGrid(result_query, gridOptions=gd.build(), reload_data=True)
    metrics_query = choice_query.melt(id_vars=['track_name',  'album_name', 'isExplicit', 'duration_ms', 'release_date'], var_name='metrics', value_name='score', value_vars=['danceability', 'energy', 'instrumentalness', 'acousticness', 'liveness', 'valence'])
    metrics_query = metrics_query.groupby(['metrics'])['score'].mean()
    metrics_query= pd.DataFrame(metrics_query).reset_index()
    fig = px.bar_polar(metrics_query, theta='metrics', r='score', range_r=[0.0,1.0], hover_name='metrics', hover_data={'score':True, 'metrics':False}, width=750, height=650, color_continuous_scale='Sunset', color='score', range_color=[0.0,1.0], template='plotly')
    fig = fig.update_layout(polar_radialaxis_gridcolor="#e3ecf6", polar_angularaxis_gridcolor="#e3ecf6", polar= dict(radialaxis= dict(showticklabels= False)), hovermode="x")
    fig = fig.update_traces(hovertemplate="<b>Metric: %{theta}<br>Score: %{r}</b>", hoverlabel= dict(bgcolor="#ffffff"))
    st.markdown('<h3>Playlist Metrics</h3>', unsafe_allow_html=True)
    metric_chart = st.plotly_chart(fig)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col2:
        
        bpm_query2 = source_data.loc[source_data['playlist_name'] == option_list, ['playlist_uri', 'tempo']]
        bpm_query2 = bpm_query2.groupby(['playlist_uri'])['tempo'].mean()
        bpm_query2 = pd.DataFrame(bpm_query2).reset_index()
        output_bpm2 = bpm_query2['tempo']
        output_bpm2 = output_bpm2.astype(int)
        if output_bpm2.sum() > 50:
            st.metric(label='Avg. BPM', value=output_bpm2)
        else:
            st.metric(label='Avg. BPM', value='Unavailable')
    with col3:
        duration_query2 = source_data.loc[source_data['playlist_name'] == option_list, ['playlist_uri', 'duration_ms']]
        output_duration2 = duration_query2.groupby(['playlist_uri'])['duration_ms'].mean()
        output_duration2 = output_duration2/60000
        output_duration2 = round(output_duration2, 2)
        st.metric(label='Avg. Track Duration (Mins)', value=output_duration2)
    with col4:
        duration_query3 = source_data.loc[source_data['playlist_name'] == option_list, ['playlist_uri', 'duration_ms']]
        output_duration3 = duration_query3.groupby(['playlist_uri'])['duration_ms'].sum()
        output_duration3 = output_duration3/60000
        output_duration3 = round(output_duration3, 2)
        st.metric(label='Total Duration (Mins)', value=output_duration3)
    
    recommendations = pd.json_normalize(sp.recommendations(seed_tracks=['spotify:track:4r8lRYnoOGdEi6YyI5OC1o'], seed_artists=['spotify:artist:6Ff53KvcvAj5U7Z1vojB5o'], limit=100, seed_genres=sp.recommendation_genre_seeds()), record_path=['tracks'])
    
    recommendations = recommendations[['name', 'album.name', 'album.release_date']]
    st.markdown('<h3>Song Recommendations</h3>', unsafe_allow_html=True)
    recommendations_df = st.write(recommendations)
            
with st.expander('Create Playlist'):
        track_search = st.text_input(label="Search for Song Name:", value="Stay")
        
        # problem with fuzzy string matching within Dataframe
        
        search_query = source_data.loc[source_data['track_name'] == track_search]
        search_query = search_query[['track_name', 'album_name', 'isExplicit', 'release_date', 'duration_ms', 'track_uri', 'album_uri']]
        gd = GridOptionsBuilder.from_dataframe(search_query)
        gd.configure_selection(selection_mode='multiple', use_checkbox=True)
        gd.configure_pagination(paginationAutoPageSize=False,paginationPageSize=10)
        gd.configure_side_bar()
        results = AgGrid(search_query, gridOptions=gd.build(), reload_data=True)
        
        # need to figure out how to maintain state
        
        final_query = pd.DataFrame(results['selected_rows'])
        if len(final_query) == 0:
            final_query = pd.DataFrame(data={'track_name':'', 'album_name':'', 'isExplicit':'', 'release_date':'', 'duration_ms':'', 'track_uri':'', 'album_uri':''}, index=range(0,len(final_query)))
        else:
            final_query = final_query[['track_name', 'album_name', 'isExplicit', 'release_date', 'duration_ms', 'track_uri', 'album_uri']]
        
        # this is a placeholder until we figure out the state handling issue
        
        final_attributes = source_data.head()

        final_attributes = final_attributes.melt(id_vars=['track_name', 'album_name', 'isExplicit'], var_name='metrics', value_name='score', value_vars=['danceability', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'valence'])
    
        final = pd.DataFrame(final_attributes.groupby(['metrics'])['score'].mean()).reset_index()
        st.markdown('<h3>Your Playlist</h3>',unsafe_allow_html=True)
        final_df = st.write(final_query)
        st.markdown('<h3>Playlist Metrics</h3>', unsafe_allow_html=True)
        fig = px.bar_polar(final, theta='metrics', r='score', range_r=[0.0,1.0], hover_name='metrics', hover_data={'score':True, 'metrics':False}, width=750, height=650, color_continuous_scale='Sunset', color='score', range_color=[0.0,1.0], template='plotly')
        fig = fig.update_layout(polar_radialaxis_gridcolor="#e3ecf6", polar_angularaxis_gridcolor="#e3ecf6", polar= dict(radialaxis= dict(showticklabels= False)), hovermode="x")
        fig = fig.update_traces(hovertemplate="<b>Metric: %{theta}<br>Score: %{r}</b>", hoverlabel= dict(bgcolor="#ffffff"))
        metric_chart = st.plotly_chart(fig)
        
        #col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
            # with col2:
            #     new_query = pd.read_sql(f"SELECT playlist_uri, AVG(audio_features2.tempo) bpm FROM test_table JOIN audio_features2 ON audio_features2.uri = test_table.track_uri WHERE playlist_uri = '{input_box}' GROUP BY playlist_uri", conn)
            #     output_bpm = new_query['bpm']
            #     output_bpm = output_bpm.astype(int)
            #     st.metric(label='Avg. BPM', value=output_bpm)
            # with col3:
            #     new_query = pd.read_sql(f"SELECT playlist_uri, AVG(audio_features2.duration_ms)/60000 duration FROM test_table JOIN audio_features2 ON audio_features2.uri = test_table.track_uri WHERE playlist_uri = '{input_box}' GROUP BY playlist_uri", conn)
            #     output_duration = new_query['duration']
            #     output_duration = output_duration.astype(float)
            #     output_duration = round(output_duration, 2)
            #     st.metric(label='Avg. Track Duration (Mins)', value=output_duration)
            # with col4:
            #     audio_features = pd.read_sql(f"SELECT playlist_uri, SUM(audio_features2.duration_ms)/60000 duration FROM test_table JOIN audio_features2 ON audio_features2.uri = test_table.track_uri WHERE playlist_uri = '{input_box}' GROUP BY playlist_uri", conn)
            #     output_duration = new_query['duration']
            #     output_duration = output_duration.astype(float)
            #     output_duration = round(output_duration, 2)
            #     st.metric(label='Total Duration (Mins)', value=output_duration)
        
        recommendations = pd.json_normalize(sp.recommendations(seed_tracks=['spotify:track:7CDd5A7FCSFIDm6eot2nEJ'], seed_artists=['spotify:artist:3NwcP2GO2sZZS2BVvWcc9T'], limit=100, seed_genres=sp.recommendation_genre_seeds()), record_path=['tracks'])
    
        recommendations = recommendations[['name', 'album.name', 'album.release_date']]
        st.markdown('<h3>Song Recommendations</h3>', unsafe_allow_html=True)
        recommendations_df = st.write(recommendations)


    

    



        
    
