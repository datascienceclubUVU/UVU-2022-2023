WITH track_count AS (
    SELECT playlist_uri, COUNT(track_uri) AS num_tracks
    FROM spotify.master
    GROUP BY playlist_uri
),

album_count AS (
    SELECT playlist_uri, COUNT(album_uri) AS num_albums
    FROM spotify.master
    GROUP BY playlist_uri
),

playlist_duration AS (
    SELECT playlist_uri, SUM(duration_ms) AS playlist_duration_ms
    FROM spotify.master
    GROUP BY playlist_uri
),

audio_features AS (
    SELECT playlist_uri, AVG(danceability) AS avg_danceability, AVG(energy) AS avg_energy,
        AVG(loudness) AS avg_loudness, AVG(acousticness) AS avg_acousticness_probability, 
        AVG(speechiness) AS avg_speechiness_probability, AVG(valence) AS avg_valence, AVG(tempo) AS avg_tempo,
        CEILING(AVG(key)) AS most_common_key, CEILING(AVG(mode)) AS most_common_mode,
        AVG(liveness) avg_liveness_probability
    FROM spotify.master
    GROUP BY playlist_uri
),


final AS (
    SELECT sm.playlist_uri, playlist_name, owner_display_name, num_tracks, num_albums, playlist_duration_ms, 
    avg_danceability, avg_energy, avg_loudness, avg_acousticness_probability, most_common_key, most_common_mode,
    avg_speechiness_probability, avg_liveness_probability, avg_valence, avg_tempo
    FROM spotify.master sm
    JOIN track_count tc ON sm.playlist_uri = tc.playlist_uri
    JOIN album_count ac ON sm.playlist_uri = ac.playlist_uri
    JOIN playlist_duration pd ON sm.playlist_uri = pd.playlist_uri
    JOIN audio_features af ON sm.playlist_uri = af.playlist_uri
)

SELECT * FROM final