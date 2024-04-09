import spotipy
import spotipy.util as util
import requests

# Spotify API credentials
CLIENT_ID = '92dfa2d52c004ffc851bd04488ac9f2d'
CLIENT_SECRET = 'b8d4a6ebd0ce48b2a9355c4c530e90b9'
REDIRECT_URI = 'http://127.0.0.1:5000'
SCOPE = 'playlist-modify-public playlist-modify-private'

# Get authorization from the user
def get_spotify_auth():
    token = util.prompt_for_user_token(
        username=None,
        scope=SCOPE,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
    return token

# Create playlist for the authenticated user
def create_playlist(access_token, playlist_name, public=True):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': playlist_name,
        'public': public
    }
    response = requests.post('https://api.spotify.com/v1/me/playlists', headers=headers, json=data)
    if response.status_code == 201:
        print("Playlist created successfully!")
    else:
        print("Error creating playlist:", response.text)

def main():
    # Step 1: Get authorization from the user
    token = get_spotify_auth()
    if token:
        print("Authorization successful!")
        # Step 2: Create playlist
        playlist_name = input("Enter playlist name: ")
        create_playlist(token, playlist_name)
    else:
        print("Authorization failed.")

if __name__ == "__main__":
    main()