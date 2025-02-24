import requests
import webbrowser
headers = {
    'Access_key' : 'aIYn6ZZ7IzbiPIAt_IF0i-ODFFC1O8lounCMUiFdg0k',
    'Secret_Key' : 'hg8FOVXOQoDQE8BVkvpO-OwmzXjh2tyioI6BJET374c',
}

url = 'https://api.unsplash.com/search/collections'
params = {
    'query' : 'Harsiddhi temple ujjain',
    'client_id' : 'aIYn6ZZ7IzbiPIAt_IF0i-ODFFC1O8lounCMUiFdg0k',
}

response = requests.get(url, headers=headers, params=params).json()

# for photo search

# for i in response["results"]:
#    image_urls = [i['urls']['raw']]
#    webbrowser.open(i['urls']['raw'])
# print(image_urls)


# for collection search
for i in response["results"]:
    cover_photo = i['cover_photo']
    urls = cover_photo['urls']
    webbrowser.open(urls['raw'])