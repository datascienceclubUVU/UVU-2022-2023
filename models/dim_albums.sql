WITH album_count AS (
    SELECT album_uri, COUNT(*) AS num_occurrences, SUM(duration_ms) AS album_duration_ms
    FROM spotify.master
    GROUP BY album_uri
),

audio_features AS (
    SELECT album_uri, AVG(danceability) AS avg_danceability, AVG(energy) AS avg_energy,
        AVG(loudness) AS avg_loudness, AVG(acousticness) AS avg_acousticness_probability,
        AVG(speechiness) AS avg_speechiness_probability, CEILING(AVG(key)) most_common_key,
        CEILING(AVG(mode)) most_common_mode, AVG(valence) AS avg_valence, AVG(tempo) AS avg_tempo
    FROM spotify.master
    GROUP BY album_uri
),

final AS (
    SELECT DISTINCT sm.album_uri, album_name, release_date, track_album_total_tracks AS num_tracks,
        num_occurrences, album_duration_ms, avg_danceability, avg_energy, avg_loudness,
        avg_acousticness_probability, avg_speechiness_probability, most_common_key, most_common_mode,
        avg_valence, avg_tempo
    FROM spotify.master sm
    JOIN album_count ac ON sm.album_uri = ac.album_uri
    JOIN audio_features af ON sm.album_uri = af.album_uri
)

SELECT * FROM final