# import requests
# url = 'https://maps.gomaps.pro/maps/api/directions/json'
# params = {
#     'key' : 'AlzaSyhAxmvv9JlozQ-mk65XlKqp_wB_la-n2Zp',
#     'destination' : 'indore',
#     'origin' : 'bhopal'
# }

# response = requests.get(url, params=params)
# print(response.json())
# print(response.url)




import requests
url = 'https://maps.gomaps.pro/maps/api/place/nearbysearch/json'
params = {
    'key' : 'AlzaSyhAxmvv9JlozQ-mk65XlKqp_wB_la-n2Zp',
    'keyword' : 'restaurant',
    
}