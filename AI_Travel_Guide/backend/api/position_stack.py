import requests

params= {
    "access_key" : '2564aefcb561827f6c3ba40de1b5ae07',

    "query" : 'vijay chat'
}
url = f'http://api.positionstack.com/v1/forward'
res = requests.get(url, params=params)
print(res.json())
print(res.url)