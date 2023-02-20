WITH all_columns AS (
    SELECT playlist_uri, track_uri, album_uri, added_at, added_by_uri, owner_uri
    FROM {{ source('core', 'master')}}
)

SELECT * FROM all_columns
