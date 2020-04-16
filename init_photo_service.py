# https://learndataanalysis.org/getting-started-with-google-photos-api-and-python-part-1/

import os
from Google import Create_Service

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

listImage = []
response = service.mediaItems().list().execute()
nextPageToken = response.get('nextPageToken')

# while nextPageToken:
#     response = service.albums.list(
#         pageSize=50,
#         excludeNonAppCreatedData=False,
#         pageToken=nextPageToken
#     )
#     listImage.append(response.get('ablums'))
#     nextPageToken = response.get('nextPageToken')

randomItemId = response.get('mediaItems')[0].get('id')
print(randomItemId)

# create dummy album
request_body = {
    'album': {'title': 'my dummy album'}
}
response_album_family_photos = service.albums().create(body=request_body).execute()

# add some image to the dummy album
itemIs = [randomItemId]
request_body = {
    'mediaItemIds': ['APbOh8-u2CWkBL88OyEzWDZvR4GkBP3tEW-0cICtWB6q1kJ9ZSAW0clrEgY1V_kCXhET85XvGy0oH47q6IpJLoxwzKjKotXfgg']
}
reponse = service.albums().batchAddMediaItems(
    albumId= response_album_family_photos.get('id'),
    body = request_body
).execute()

print(response)