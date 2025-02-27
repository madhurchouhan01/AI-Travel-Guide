response = {
    "total": 237,
    "total_pages": 12,
    "results": [
      {
        "id": 193913,
        "title": "Office",
        "description": None,
        "published_at": "2016-04-15T21:05:44-04:00",
        "last_collected_at": "2016-06-02T13:10:03-04:00",
        "updated_at": "2016-07-10T11:00:01-05:00",
        "featured": True,
        "total_photos": 60,
        "private": False,
        "share_key": "79ec77a237f014935eddc774f6aac1cd",
        "cover_photo": {
          "id": "pb_lF8VWaPU",
          "created_at": "2015-02-12T18:39:43-05:00",
          "width": 5760,
          "height": 3840,
          "color": "#1F1814",
          "blur_hash": "L14Bk2M{0d^lR*j[ofWB0K%3^l9Y",
          "likes": 786,
          "liked_by_user": False,
          "description": "A man drinking a coffee.",
          "user": {
            "id": "tkoUSod3di4",
            "username": "gilleslambert",
            "name": "Gilles Lambert",
            "first_name": "Gilles",
            "last_name": "Lambert",
            "instagram_username": "instantgrammer",
            "twitter_username": "gilleslambert",
            "portfolio_url": "http://www.gilleslambert.be/photography",
            "profile_image": {
              "small": "https://images.unsplash.com/profile-1445832407811-c04ed64d238b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32&s=4bb8fad0dcba43c46491c6fd0b92f537",
              "medium": "https://images.unsplash.com/profile-1445832407811-c04ed64d238b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64&s=a6d8602c855914fe13650eedd5996cb5",
              "large": "https://images.unsplash.com/profile-1445832407811-c04ed64d238b?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=26099ca5069692aac6973d08ae02dd71"
            },
            "links": {
              "self": "https://api.unsplash.com/users/gilleslambert",
              "html": "http://unsplash.com/@gilleslambert",
              "photos": "https://api.unsplash.com/users/gilleslambert/photos",
              "likes": "https://api.unsplash.com/users/gilleslambert/likes"
            }
          },
          "urls": {
            "raw": "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a",
            "full": "https://hd.unsplash.com/photo-1423784346385-c1d4dac9893a",
            "regular": "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&s=d60d527cb347746ab3abf5fccecf0271",
            "small": "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&s=0bf0c97abca8b2741380f38d3debd45f",
            "thumb": "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=9bc3a6d42a16809b735c22720de3fb13"
          },
          "links": {
            "self": "https://api.unsplash.com/photos/pb_lF8VWaPU",
            "html": "http://unsplash.com/photos/pb_lF8VWaPU",
            "download": "http://unsplash.com/photos/pb_lF8VWaPU/download"
          }
        },
        "user": {
          "id": "k_gSWNtOjS8",
          "username": "cjmconnors",
          "name": "Christine Connors",
          "portfolio_url": None,
          "bio": "",
          "profile_image": {
            "small": "https://images.unsplash.com/placeholder-avatars/extra-large.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32&s=0ad68f44c4725d5a3fda019bab9d3edc",
            "medium": "https://images.unsplash.com/placeholder-avatars/extra-large.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64&s=356bd4b76a3d4eb97d63f45b818dd358",
            "large": "https://images.unsplash.com/placeholder-avatars/extra-large.jpg?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128&s=ee8bbf5fb8d6e43aaaa238feae2fe90d"
          },
          "links": {
            "self": "https://api.unsplash.com/users/cjmconnors",
            "html": "http://unsplash.com/@cjmconnors",
            "photos": "https://api.unsplash.com/users/cjmconnors/photos",
            "likes": "https://api.unsplash.com/users/cjmconnors/likes"
          }
        },
        "links": {
          "self": "https://api.unsplash.com/collections/193913",
          "html": "http://unsplash.com/collections/193913/office",
          "photos": "https://api.unsplash.com/collections/193913/photos",
          "related": "https://api.unsplash.com/collections/193913/related"
        }
      }
    ]
  }
img = []
for i in response["results"]:
    cover_photo = i['cover_photo']
    urls = cover_photo['urls']
    img.append(urls['raw'])
print(img)