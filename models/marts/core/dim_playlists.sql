{{
    config(
        materialized='table'
    )
}}

WITH track_count AS (
    SELECT DISTINCT playlist_uri, COUNT(track_uri) AS num_tracks
    FROM {{ source('core', 'fact_playlist_tracks') }}
    GROUP BY playlist_uri
),

album_count AS (
    SELECT DISTINCT playlist_uri, COUNT(album_uri) AS num_albums
    FROM {{ source('core', 'fact_playlist_tracks')}}
    GROUP BY playlist_uri
),

duration AS (
    SELECT DISTINCT playlist_uri, SUM(duration_ms) AS total_duration
    FROM {{ source('core', 'master') }}
    GROUP BY playlist_uri
),

final AS (
    SELECT DISTINCT sm.playlist_uri, playlist_name, owner_display_name, num_tracks, num_albums, 
    followers_total, total_duration
    FROM {{ source('core', 'master') }} sm
    JOIN track_count tc ON sm.playlist_uri = tc.playlist_uri
    JOIN album_count ac ON sm.playlist_uri = ac.playlist_uri
    JOIN duration d ON sm.playlist_uri = d.playlist_uri
)

SELECT * FROM final