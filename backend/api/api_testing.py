import requests
API_KEY = "f210cbe2c2548d22f0d26c1630f5439b"
city = "Indore"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response = requests.get(url)
print(response.json())
