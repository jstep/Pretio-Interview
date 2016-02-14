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
    API_KEY = "c00d0814f0b548c68817473b1605a375"

    # Country Code.
    gi = pygeoip.GeoIP("static/GeoIP.dat")  # Lookup for country codes. Obtained from http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
    if request.headers.getlist("X-Forward-For"):
        ip = request.headers.getlist("X-Forward-For")[0]
    else:
        ip = request.environ['REMOTE_ADDR']
        ip = "104.142.123.45"
        print "ip : " + ip

    cc = "&country_code={}".format(gi.country_code_by_addr(ip))
    # cc = "&country_code=US"

    # HTTP Post.
    base_url = "https://offers.pretio.in/publishers/{}/api/?user_id=12345{}".format(API_KEY, cc)
    headers = {'content-type': 'application/json'}
    response = requests.post(base_url, headers=headers)
    url = response.json()['url']

    return render_template('ad.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)
