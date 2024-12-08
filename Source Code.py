import requests
import base64

# Client ID and redirect URI
CLIENT_ID = ''
REDIRECT_URI = ''

# Spotify Authorization URL
AUTH_URL = 'https://accounts.spotify.com/authorize'

# Authorization request URL
params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': 'user-library-read playlist-read-private user-read-private user-read-email'
}

auth_request_url = f"{AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in params.items())}"

print("Please visit this URL and authorize the app:")
print(auth_request_url)

import requests
import base64

# Spotify API credentials
client_id = ' '
client_secret = ''
redirect_uri = ''
auth_code = ''

# Encode the client ID and client secret
auth_str = f"{client_id}:{client_secret}"
auth_bytes = auth_str.encode('utf-8')
auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

# Exchange code for token
auth_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': 'Basic ' + auth_base64,
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri
}

response = requests.post(auth_url, headers=headers, data=data)
tokens = response.json()
access_token = tokens['access_token']

# Function to get saved albums
def get_saved_albums():
    endpoint = 'https://api.spotify.com/v1/me/albums'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint, headers=headers)
    return response.json()

# Function to get liked songs
def get_liked_songs():
    endpoint = 'https://api.spotify.com/v1/me/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint, headers=headers)
    return response.json()

# Function to get playlists
def get_playlists():
    endpoint = 'https://api.spotify.com/v1/me/playlists'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint, headers=headers)
    return response.json()

# Fetch and display user data
saved_albums = get_saved_albums()
print("User's Saved Albums:")
for album in saved_albums['items']:
    print(f" - {album['album']['name']} by {', '.join(artist['name'] for artist in album['album']['artists'])}")

liked_songs = get_liked_songs()
print("User's Liked Songs:")
for song in liked_songs['items']:
    print(f" - {song['track']['name']} by {', '.join(artist['name'] for artist in song['track']['artists'])}")

playlists = get_playlists()
print("User's Playlists:")
for playlist in playlists['items']:
    print(f" - {playlist['name']} (ID: {playlist['id']})")
