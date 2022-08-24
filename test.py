import requests
import pprint
import json
search = input('please give search: ').replace(" ", "+")

par_aic = {
    'q': search
}
par_artsy = {
    'q': search +"+more:pagemap:metatags-og_type:artwork"
}

client_id = '779562f6b5e73c011e67'
client_secret = 'ffbc3e7b519e84cbcd7578ffd80b2574'
api_url = 'https://api.artsy.net/api/tokens/xapp_token'

# Catches token
r = requests.post(api_url, data={"client_id":client_id, "client_secret":client_secret})

j = json.loads(r.text)
token = j["token"]

# Connects and Requests information
head = {"X-Xapp-Token": token}

#artsy = requests.get("https://api.artsy.net/api/search?q=Andy+Warhol+more:pagemap:metatags-og_type:artist", headers=head)
aic = requests.get("https://api.artic.edu/api/v1/artworks/search",params=par_aic)
# artsy_data = artsy.json()

aic_data = aic.json()['data']

print()
pprint.pprint(aic_data)
print()
for x in aic_data:
    title = x['title']
    imreq = requests.get("https://api.artic.edu/api/v1/artworks/"+str(x["id"]),params={"fields": "image_id"})
    image = "https://www.artic.edu/iiif/2/"+ str(imreq.json()["data"]["image_id"]) +"/full/843,/0/default.jpg"
    print(image)

# for x in artsy_data:
#     title = x['title']
#     artist = 
#     image = x['link']['thumbnail']
