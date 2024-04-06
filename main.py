import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
import csv
import pandas

# Spotify API credentials
client_id = 'f1fdd145259a4e4692898ec671ad98ce'
client_secret = '6a300bfe0d9d47b6ba41ca6383a1c1a5'
redirect_uri = 'http://localhost:8888/callback'

# Getting the Track URIs
dataset = pandas.read_csv("tracksInSpotify.csv")
dataset = pandas.Series.tolist(dataset)
    
    # Initialize empty lists to store tracks and reformatted data
trackURIs = []
trackMood = []
formatted_track_URIs = []
    # Iterate over each element in the dataset
for elem in dataset:
        # Strip brackets and single quotes, then split by comma and space to get individual items
    res = elem[0].strip('][').replace("'", "").split(', ')
    trackURIs.append(res[0])  # Append the reformatted data to the data list
    trackMood.append(res[1])  # Append the track name to the tracks list
for i, mood in enumerate(trackMood):
    #check if mood is sad
    if mood == "sad":
        spotify_uri = f"spotify:track:{trackURIs[i]}"
        # Add the formatted URI to the new list
        formatted_track_URIs.append(spotify_uri)
        
    
    
    # Return the tracks list and the reformatted data list
#print(trackURIs, trackMood)

# Create Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= 'f1fdd145259a4e4692898ec671ad98ce', client_secret='6a300bfe0d9d47b6ba41ca6383a1c1a5', redirect_uri='http://localhost:8888/callback'))

# Get user ID
user_id = sp.current_user()['id']

# Create a new playlist
playlist_name = 'My Playlist'
playlist = sp.user_playlist_create(user_id, playlist_name)

# Add the track to the playlist
batch_size = 100

# Add tracks to the playlist in batches
for i in range(0, len(formatted_track_URIs), batch_size):
    batch = formatted_track_URIs[i:i+batch_size]
    sp.playlist_add_items(playlist['id'], batch)
#sp.playlist_add_items(playlist['id'], formatted_track_URIs)

print("Playlist created successfully!")
