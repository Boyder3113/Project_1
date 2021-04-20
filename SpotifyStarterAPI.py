import requests
import json

baseAddress = "https://api.spotify.com"
fullAddress = baseAddress

response = requests.get(baseAddress).json()

print(response)

