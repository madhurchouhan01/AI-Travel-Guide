import requests
import webbrowser
count = 20
fsq_id = ['4cbe72be8db3b60cfe9b7278','50f11526e4b0f9cd32576bcd','4d6fb9b527316ea8c63bb4aa','645bc0fa15e91f362e0d7d64','4b7799f3f964a5206ba32ee3','4ff90b33e4b0d61584e8f7ab','58581b9551d19e305314df57','4f257ec2e4b01dc94cadd76f','4fe54ee9e4b0ec3d84c504da','51f3aaf8498eab595a421bd6','50a8dc2fe4b0702a82cbe73b','4fa14735e4b0e1be2a8ed91e','511899bfe4b08ffa4fbacd18','577cb5aacd10c1e61164cc80','5cda853625fb7b002be4644d','4c716ae3df6b8cfa49ffba4d','619e59c40fb05b41f7f30fbc','4fce3699e4b0f39fffe34fdb','63bd1578c6b40f4b8a5359de','4ef832ff6c25c411ebdc7dac',]

    
# API URL and headers
url = "https://api.foursquare.com/v3/places/photos"
headers = {
    "accept": "application/json",
    "Authorization": "fsq3RC+0Z66+nluxJf4T5TyDuK6LGyOBnGHcp3TFdisLc28="
}

for i in fsq_id:
    url = f'https://api.foursquare.com/v3/places/{i}/photos'
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        photos = response.json()
        for photo in photos:
            photo_url = f"{photo['prefix']}original{photo['suffix']}"
            print(photo_url)
            webbrowser.open(photo_url)
    else:
        print(f"Failed to fetch photos: {response.status_code}")

