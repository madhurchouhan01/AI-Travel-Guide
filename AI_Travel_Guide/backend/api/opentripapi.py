import requests
api_key = "5ae2e3f221c38a28845f05b6269d167a5b94613dbb3518229d0b03da"


url = "https://api.opentripmap.com/0.1/en/places/radius"
params = {
    "radius": 5000,  # Radius in meters
    "lon": 75.8577,  # Longitude
    "lat": 22.7196,  # Latitude
    "apikey": api_key
}
response = requests.get(url, params=params)
print(response.json())
