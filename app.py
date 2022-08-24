from flask import Flask, render_template, request, url_for, redirect
import requests
import sys
import pprint
import json

# artsy = requests.get("https://api.artsy.net/api/search")
# aic = requests.get("https://api.artic.edu/api/v1/artworks/search")

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        print(search, file=sys.stderr)
        par_aic = {
            'q': search
        }
        # par_artsy = {
        #     'q': search +"+more:pagemap:metatags-og_type:artwork"
        # }

        # client_id = '779562f6b5e73c011e67'
        # client_secret = 'ffbc3e7b519e84cbcd7578ffd80b2574'
        # api_url = 'https://api.artsy.net/api/tokens/xapp_token'

        # # Catches token
        # r = requests.post(api_url, data={"client_id":client_id, "client_secret":client_secret})

        # j = json.loads(r.text)
        # token = j["token"]

        # # Connects and Requests information
        # head = {"X-Xapp-Token": token}

        #artsy = requests.get("https://api.artsy.net/api/search",params=par_artsy, headers=head)
        aic = requests.get("https://api.artic.edu/api/v1/artworks/search",params=par_aic)
        #artsy_data = artsy.json()

        aic_data = aic.json()['data']
        results = []
        for i in range(len(aic_data)):
            res = {
                "title": '',
                "image": ''
            }
            res["title"] = aic_data[i]['title']
            imreq = requests.get("https://api.artic.edu/api/v1/artworks/"+str(aic_data[i]["id"]),params={"fields": "image_id"})
            image = "https://www.artic.edu/iiif/2/"+ str(imreq.json()["data"]["image_id"]) +"/full/843,/0/default.jpg"
            print(image, file=sys.stderr)
            res['image'] = image
            results.append(res)
        return render_template('result.html', results = results) 

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)