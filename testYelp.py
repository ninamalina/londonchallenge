import io
import json
import rauth

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


params = get_search_parameters(51.502096, -0.024820)

request = session.get("http://api.yelp.com/v2/search", params=params)
data = request.json()
session.close()

print data