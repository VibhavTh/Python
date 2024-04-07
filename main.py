import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import tkinter as tk
import csv
import pandas
import os
import sys
import MoodFilter


# Spotify API credentials and authenticating with Spotify
client_id = 'f1fdd145259a4e4692898ec671ad98ce'
client_secret = '6a300bfe0d9d47b6ba41ca6383a1c1a5'
redirect_uri = 'http://localhost:8888/callback'
#username = 'pxta1twk8u48a98qiho2mll7n'
#"315jvettju53yj3hwn3f66x64ibq" - test account username
'''
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Please supply a user ID")
    sys.exit()
    
scopes = " user-top-read user-library-modify user-library-read user-read-private playlist-read-private playlist-modify-public playlist-modify-private user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming user-follow-read user-follow-modify"

# Prompt for user permission
try:
    token = util.prompt_for_user_token(username, scopes,
                                       client_id='f1fdd145259a4e4692898ec671ad98ce',
                                       client_secret='6a300bfe0d9d47b6ba41ca6383a1c1a5',
                                       redirect_uri='http://localhost:8888/callback')
except:
    os.remove(".cache-{}".format(username))
    token = util.prompt_for_user_token(username, scopes,
                                       client_id='f1fdd145259a4e4692898ec671ad98ce',
                                       client_secret='6a300bfe0d9d47b6ba41ca6383a1c1a5',
                                       redirect_uri='http://localhost:8888/callback')

# Get user ID
if token:
	#define spotify object and user
	sp = spotipy.Spotify(auth=token)
	user = sp.current_user()
    
user_id = input("Enter the target user's Spotify user ID: ")
'''
# Create Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= 'f1fdd145259a4e4692898ec671ad98ce', client_secret='6a300bfe0d9d47b6ba41ca6383a1c1a5', redirect_uri='http://localhost:8888/callback'))

# Get user ID
user_id = sp.current_user()['id']

FINAL_formatted_track_URIs = MoodFilter.random_formatted_track_URIs
FINAL_userMood = MoodFilter.songMood.upper()
# Create a new playlist
playlist_name = FINAL_userMood + ' Playlist'
playlist = sp.user_playlist_create(user_id, playlist_name)

# Add the track to the playlist
batch_size = 100

# Add tracks to the playlist in batches
for i in range(0, len(FINAL_formatted_track_URIs), batch_size):
    batch = FINAL_formatted_track_URIs[i:i+batch_size]
    sp.playlist_add_items(playlist['id'], batch)

print("Playlist created successfully!")