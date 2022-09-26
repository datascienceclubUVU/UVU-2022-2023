## To Create the Initial Database, Copy and Paste the following Code:

CREATE DATABASE Spotify;

## To Create the Master Table, Copy and Paste the following Code:

USE Spotify;

CREATE TABLE master ( pid BIGINT, pos INT, track_name VARCHAR(MAX), artist_name VARCHAR(MAX), album_name VARCHAR(MAX), track_uri VARCHAR(MAX), artist_uri VARCHAR(MAX), album_uri VARCHAR(MAX), duration_ms BIGINT, PRIMARY KEY (pid, pos));

## To Create the Playlists Table, Copy and Paste the following Code:

USE Spotify;

CREATE TABLE playlists ( pid BIGINT, name VARCHAR(MAX), num_tracks INT, num_artists INT, num_albums INT, num_edits INT, num_followers INT, modified_at BIGINT, duration_ms BIGINT, collaborative BIT, description VARCHAR(MAX), PRIMARY KEY (pid));

## To Create the Tracks Table, Copy and Paste the following Code:

USE Spotify;

CREATE TABLE tracks ( track_name VARCHAR(MAX), artist_name VARCHAR(MAX), album_name VARCHAR(MAX), track_uri VARCHAR(MAX), PRIMARY KEY (track_uri));
