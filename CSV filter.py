

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
        spotify_uri = f"spotify:track:{i}"
        # Add the formatted URI to the new list
        formatted_track_URIs.append(spotify_uri)
        
        print(formatted_track_URIs)
    
    # Return the tracks list and the reformatted data list
#print(trackURIs, trackMood)


