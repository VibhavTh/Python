import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import json
import time
import pandas as pd

 # Credentials you get from registering a new application
client_id = '92dfa2d52c004ffc851bd04488ac9f2d'
client_secret = 'b8d4a6ebd0ce48b2a9355c4c530e90b9'
redirect_uri = 'http://127.0.0.1:5000/redirect'
# OAuth endpoints given in the Spotify API documentation
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = [
    "user-read-email",
    "playlist-read-collaborative",
    "playlist-modify-public",
    "playlist-modify-private"
]

from requests_oauthlib import OAuth2Session
spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

app = Flask(__name__)
# Redirect user to Spotify for authorization
authorization_url, state = spotify.authorization_url(authorization_base_url)
print('Please go here and authorize: ', authorization_url)

@app.route('/')
def index():
    return redirect(authorization_url)

@app.route('/redirect')
def redirect_page():
    redirect_response = request.url
    token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
    session['token'] = token
    return redirect('/profile')
        
# Get the authorization verifier code from the callback url

from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(client_id, client_secret)

@app.route('/profile')
def profile():
    if 'token' in session:
        token = session['token']
        spotify = OAuth2Session(client_id, token=token)
        r = spotify.get('https://api.spotify.com/v1/me')
        return r.text
    else:
        return 'Token not found!'

 # Fetch the access token


if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)


#!/usr/bin/python3

