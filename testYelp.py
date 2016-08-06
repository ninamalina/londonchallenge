import io
import json
import rauth
from urllib2 import urlopen
import json


def get_search_parameters(lat, long):
    # See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "10"

    return params


with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    session = rauth.OAuth1Session(**creds)


f = urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
print(location)
lat = location['latitude']
lon = location['longitude']

print lat, lon

params = get_search_parameters(lat, lon)

request = session.get("http://api.yelp.com/v2/search", params=params)
data = request.json()
session.close()

print data



