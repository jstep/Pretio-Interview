from flask import Flask, render_template, request
import pygeoip
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ad')
def serve_ad():
    # TODO: Obscure api key with a config file.
    apikey = "c00d0814f0b548c68817473b1605a375"

    # Country Code.
    gi = pygeoip.GeoIP("static/GeoIP.dat")  # Lookup for country codes. Obtained from http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
    cc = gi.country_code_by_addr(request.remote_addr)
    cc = 'CA'  # TODO: Delete when done testing and deployed.

    # HTTP Post.
    base_url = "https://offers.pretio.in/publishers/{}/api/?user_id=12345&country_code={}".format(apikey, cc)
    headers = {'content-type': 'application/json'}
    response = requests.post(base_url, headers=headers)
    url_req = response.json()['url']
    print url_req

    return render_template('ad.html', url=url_req)

if __name__ == '__main__':
    app.run()
