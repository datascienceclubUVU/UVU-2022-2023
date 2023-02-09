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
    SELECT DISTINCT tc.track_uri, track_name, album_name, track_album_album_type AS track_type, release_date,
        "isExplicit", duration_ms AS track_duration_ms, track_preview_url, tc.num_occurrences,
        danceability, energy, loudness, acousticness, speechiness, liveness, key, mode, valence, tempo
    FROM {{ source('core', 'master') }} sm
    JOIN track_count tc ON sm.track_uri = tc.track_uri
)

SELECT * FROM final