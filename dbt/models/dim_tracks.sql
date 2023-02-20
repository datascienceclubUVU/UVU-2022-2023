{{
    config(
        materialized='table'
    )
}}

WITH track_count AS (
    SELECT DISTINCT track_uri, COUNT(*) AS num_occurrences
    FROM {{ source('core', 'fact_playlist_tracks')}}
    GROUP BY track_uri
),

final AS (
    SELECT DISTINCT tc.track_uri, track_name, artist1, artist2, artist3, artist4, artist5, album_name, 
    release_date, "isExplicit", duration_ms AS track_duration_ms, 
    track_popularity AS popularity_rating, track_preview_url, tc.num_occurrences, danceability, energy, 
    loudness, acousticness, speechiness, liveness, key, mode, valence, tempo, time_signature
    FROM {{ source('core', 'master') }} sm
    JOIN track_count tc ON sm.track_uri = tc.track_uri
)

SELECT * FROM final
