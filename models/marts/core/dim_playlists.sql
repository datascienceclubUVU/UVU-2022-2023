{{
    config(
        materialized='table'
    )
}}

WITH final AS (
    SELECT DISTINCT sm.playlist_uri, playlist_name, owner_display_name, num_tracks, num_albums, playlist_duration_ms, 
    avg_danceability, avg_energy, avg_loudness, avg_acousticness_probability, most_common_key, most_common_mode,
    avg_speechiness_probability, avg_liveness_probability, avg_valence, avg_tempo
    FROM spotify.master sm
    JOIN track_count tc ON sm.playlist_uri = tc.playlist_uri
    JOIN album_count ac ON sm.playlist_uri = ac.playlist_uri
    JOIN playlist_duration pd ON sm.playlist_uri = pd.playlist_uri
    JOIN audio_features af ON sm.playlist_uri = af.playlist_uri
)

SELECT * FROM final