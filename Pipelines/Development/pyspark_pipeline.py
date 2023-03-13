from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, BooleanType

# Create a SparkSession
spark = SparkSession.builder.appName("Spotify Pipeline").getOrCreate()

# Define the schema for the tracks DataFrame
tracks_schema = StructType([
    StructField("playlist_uri", StringType(), True),
    StructField("track_name", StringType(), True),
    StructField("track_uri", StringType(), True),
    StructField("album_name", StringType(), True),
    StructField("isExplicit", BooleanType(), True),
    StructField("release_date", StringType(), True),
    StructField("duration_ms", DoubleType(), True),
    StructField("album_uri", StringType(), True),
    StructField("added_by_external_urls_spotify", StringType(), True),
    StructField("added_by_href", StringType(), True),
    StructField("added_by_id", StringType(), True),
    StructField("added_by_type", StringType(), True),
    StructField("added_by_uri", StringType(), True),
    StructField("track_album_album_type", StringType(), True),
    StructField("track_album_external_urls_spotify", StringType(), True),
    StructField("track_album_href", StringType(), True),
    StructField("track_album_id", StringType(), True),
    StructField("track_album_release_date_precision", StringType(), True),
    StructField("track_album_total_tracks", DoubleType(), True),
    StructField("track_album_type", StringType(), True),
    StructField("track_disc_number", DoubleType(), True),
    StructField("track_episode", BooleanType(), True),
    StructField("track_external_ids_isrc", StringType(), True),
    StructField("track_external_ids_spotify", StringType(), True),
    StructField("track_href", StringType(), True),
    StructField("track_id", StringType(), True),
    StructField("track_is_local", BooleanType(), True),
    StructField("track_popularity", DoubleType(), True),
    StructField("track_preview_url", StringType(), True),
    StructField("track_track", BooleanType(), True),
    StructField("track_track_number", DoubleType(), True),
    StructField("track_type", StringType(), True),
    StructField("video_thumbnail_url", StringType(), True),
    StructField("external_urls_spotify", StringType(), True),
    StructField("followers_href", StringType(), True),
    StructField("followers_total", DoubleType(), True),
    StructField("owner_display_name", StringType(), True),
    StructField("owner_external_urls_spotify", StringType(), True),
    StructField("owner_href", StringType(), True),
    StructField("owner_id", StringType(), True),
    StructField("owner_type", StringType(), True),
    StructField("owner_uri", StringType(), True),
    StructField("tracks_href", StringType(), True),
    StructField("tracks_limit", DoubleType(), True),
    StructField("tracks_next", StringType(), True),
    StructField("tracks_offset", DoubleType(), True),
    StructField("tracks_previous", StringType(), True),
    StructField("tracks_total", DoubleType(), True),
    StructField("playlist_name", StringType(), True)
])

# Read the distinct_playlists.csv file into a DataFrame
new_batch = spark.read.csv("distinct_playlists.csv", header=True, inferSchema=True).select("playlist_uri", "playlist_name")

# Strip whitespace from the playlist_uri column
new_batch = new_batch.withColumn("playlist_uri", col("playlist_uri").trim())

# Load the playlist_uris already in the database
db_batch = spark.read.csv("db_playlist_uris.csv", header=True, inferSchema=True).select("playlist_uri")

# Filter out the playlists that are already in the database
new_batch = new_batch.join(db_batch, on="playlist_uri", how="leftanti")

# Read the tracks.csv file into a DataFrame
tracks = spark.read.csv("tracks.csv", header=True, schema=tracks_schema).select("playlist_uri", "track_name", "track_uri", "album_name", "isExplicit", "release_date", "duration_ms", "album_uri")

# Join the new_batch DataFrame with the tracks DataFrame
new_batch = new_batch.join(tracks, on="playlist_uri", how="inner")

# Write the new batch to the database
new_batch.write.jdbc(
    url="jdbc:postgresql://localhost:5432/spotify",
    table="tracks",
    mode="append",
    properties={
        "user": "postgres",
        "password": "password"
    }
)

# Write the new playlist_uris to the database
new_batch.select("playlist_uri").write.jdbc(
    url="jdbc:postgresql://localhost:5432/spotify",
    table="playlist_uris",
    mode="append",
    properties={
        "user": "postgres",
        "password": "password"
    }
)

# Stop the SparkSession
spark.stop()