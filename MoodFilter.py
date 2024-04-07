import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import tkinter as tk
import csv
import pandas
import os
import sys
import random


# Getting the Track URIs
dataset = pandas.read_csv("tracksInSpotify.csv")
dataset = pandas.Series.tolist(dataset)
        
    # Initialize empty lists to store tracks and reformatted data
trackURIs = []
trackMood = []
formatted_track_URIs = []

valid_choices = ["1", "2"]


print("Please select which mode you want:")
print("1. Normal - Your playlist will match the mood you select")
print("2. Random - Your playlist's mood will be chosen randomly")
print("")
while True:
    userMode = input("Enter the corresponding number for your choice: ")
    if userMode in valid_choices:
        if userMode == '1':
            normal_valid_choices = ["1", "2", "3", "4"]
            songMood = ''
            
            print("")
            print("Please enter the mood you want your music to be in:")
            print("1. Happy")
            print("2. Sad")
            print("3. Angry")
            print("4. Relaxed")
            print("")
            while True:
                userMood = input("Enter the corresponding number for your choice: ")
                if userMood in normal_valid_choices:
                    if userMood == '1':
                        songMood = "happy"
                    elif userMood == "2":
                        songMood = "sad"
                    elif userMood == "3":
                        songMood = "angry"
                    elif userMood == "4":
                        songMood = "relaxed"
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            print("You selected:", songMood)
        elif userMode == '2':
            moods = ['happy', 'sad', 'angry', 'relaxed']
            songMood = random.choice(moods)
            print("You selected:", songMood)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
    




       
    # Iterate over each anelement in the dataset
for elem in dataset:
    # Strip brackets and single quotes, then split by comma and space to get individual items
    res = elem[0].strip('][').replace("'", "").split(', ')
    trackURIs.append(res[0])  # Append the reformatted data to the data list
    trackMood.append(res[1])  # Append the track name to the tracks list
for i, mood in enumerate(trackMood):
    #check if mood is sad
    if mood == songMood:
        spotify_uri = f"spotify:track:{trackURIs[i]}"
        # Add the formatted URI to the new list
        formatted_track_URIs.append(spotify_uri)
            
# Randomly chooses 10 songs from the new formatted list to create final form of the playlist to use in main.py      
random_formatted_track_URIs = random.sample(formatted_track_URIs, k=10)
       

