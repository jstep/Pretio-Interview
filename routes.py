from flask import Flask, render_template, request
import pygeoip
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ad')
def serve_ad():
    # TODO: Obscure api key with a config file. And destroy this key.
    API_KEY = "c00d0814f0b548c68817473b1605a375"

    gi = pygeoip.GeoIP("static/GeoIP.dat")  # Lookup for country codes. Obtained from http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz

    # Get real client IP if behind proxy (like Heroku).
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[-1]
    else:
        ip = request.remote_addr

    # Country Code. Default for localhost.
    if gi.country_code_by_addr(ip):
        cc = "&country_code={}".format(gi.country_code_by_addr(ip))
    else:
        cc = "&country_code=CA"

    # HTTP Post.
    base_url = "https://offers.pretio.in/publishers/{}/api/?user_id=12345{}".format(API_KEY, cc)
    headers = {'content-type': 'application/json'}
    response = requests.post(base_url, headers=headers)
    url = response.json()['url']

    return render_template('ad.html', url=url)

if __name__ == '__main__':
    app.run()
