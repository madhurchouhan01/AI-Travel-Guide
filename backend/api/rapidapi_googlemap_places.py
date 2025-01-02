import requests

url = "https://google-map-places.p.rapidapi.com/maps/api/geocode/json"

querystring = {"address":"indore","language":"en","region":"en","result_type":"administrative_area_level_1","location_type":"APPROXIMATE"}

headers = {
	"x-rapidapi-key": "86c99d5173mshde72a02f5868513p14605bjsn8d4889ca700d",
	"x-rapidapi-host": "google-map-places.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())