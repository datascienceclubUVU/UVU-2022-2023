{{
    config(
        materialized='table'
    )
}}

WITH album_count AS (
    SELECT DISTINCT album_uri, COUNT(*) AS num_occurrences
    FROM {{ source('core', 'fact_playlist_tracks') }}
    GROUP BY album_uri
),

audio_features AS (
    SELECT album_uri, AVG(danceability) AS avg_danceability, AVG(energy) AS avg_energy,
        AVG(loudness) AS avg_loudness, AVG(acousticness) AS avg_acousticness_probability,
        AVG(speechiness) AS avg_speechiness_probability, CEILING(AVG(key)) most_common_key,
        CEILING(AVG(mode)) most_common_mode, AVG(valence) AS avg_valence, AVG(tempo) AS avg_tempo, SUM(duration_ms) album_duration_ms
    FROM {{ source('core', 'master') }}
    GROUP BY album_uri
),

final AS (
    SELECT DISTINCT ROW_NUMBER() OVER(PARTITION BY sm.album_uri ORDER BY sm.album_uri) row_num, sm.album_uri, album_name, 
    artist1, artist2, artist3, release_date, track_album_total_tracks AS num_tracks,
        num_occurrences, album_duration_ms, avg_danceability, avg_energy, avg_loudness,
        avg_acousticness_probability, avg_speechiness_probability, most_common_key, most_common_mode,
        avg_valence, avg_tempo
    FROM spotify.master sm
    JOIN album_count ac ON sm.album_uri = ac.album_uri
    JOIN audio_features af ON sm.album_uri = af.album_uri
)

SELECT album_uri, album_name, artist1, artist2, artist3, release_date, num_tracks, 
num_occurrences, album_duration_ms, avg_danceability, avg_energy, avg_loudness, avg_acousticness_probability,
avg_speechiness_probability, most_common_key, most_common_mode, avg_valence, avg_tempo
FROM final WHERE row_num = 1