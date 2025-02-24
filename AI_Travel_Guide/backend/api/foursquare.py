api_key = 'fsq3RC+0Z66+nluxJf4T5TyDuK6LGyOBnGHcp3TFdisLc28='

import requests
def recommend_api(latitude, longitude, radius, budget):
    print('inside recommend api function')
    if budget <= 10000:
        max_price = 1
    elif budget <= 20000:
        max_price = 2
    elif budget <= 30000:
        max_price = 3
    elif budget >= 40000:
        max_price = 4
    url = "https://api.foursquare.com/v3/places/search"

    headers = {
        "accept": "application/json",
        "Authorization": "fsq3RC+0Z66+nluxJf4T5TyDuK6LGyOBnGHcp3TFdisLc28="
    }

    param = {
        'radius' : radius*1000,
        'll' : f'{latitude},{longitude}',
        # 'max_price' : max_price,
        'categories' : f'{12103},{16000},{16034},{10000},{12081},{12106},{12108},{12111},{12124}',
        'sort': 'POPULARITY',
        'limit': 20
    }
    response = requests.get(url, headers=headers, params=param)
    return response.json()

# recommend_api(22.7195687, 75.8577258, 50, 2000)
