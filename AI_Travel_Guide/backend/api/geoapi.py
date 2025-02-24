# import requests
# url = f"https://api.geoapify.com/v1/geocode/search?text=New York&apiKey={API_KEY}"
# response = requests.get(url)
# print(response.json())

import requests

API_KEY = "e7caa474b0124c3c90a2834eec0d4ba1"
url = "https://api.geoapify.com/v2/places?categories=commercial.shopping_mall&filter=circle:75.86419512493137,22.717417620169968,5000&bias=proximity:75.86419512493137,22.717417620169968&lang=en&limit=20&apiKey=e7caa474b0124c3c90a2834eec0d4ba1"
          
response = requests.get(url)
print(response.json())
