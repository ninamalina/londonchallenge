import io
import json
import rauth
from urllib2 import urlopen
import json
import facebook


def get_search_parameters(lat, long):
    # See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat), str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "20"

    return params


times = ["timeToGoToWork", "lunchTime", "timeToGoHome", "nothingSpecial"]
time = "lunchTime"

"""get fb info"""

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAIY0fH3jUcFDXCogKTB1dLgSdslVFROfRPg97eCVaQZCgUss6r5cmaVXZCKqu2iADhd9fxhuFVTdb8vv3sNqU6bRj6ZC0Spd8dujZAj53hCYh5ZAQUZBJzzSdCSsZCOZBsjIbbyjyusZB9ereAKQ3i3AmLOfIdT8qBAZDZD', version='2.2');
user = graph.get_object("me")

first_name = user['first_name']
last_name = user['last_name']
email = user['email']
birthday = user['birthday']
relationship_status = user['relationship_status']

likes = graph.get_object("me/likes")

likes_list = []
while 'next' in likes['paging']:
    for like in likes['data']:
        likes_list.append(like)

    likes = graph.get_object("me/likes?after=" + likes['paging']['cursors']['after'])

food_likes = []
liked_categories = []

for like in likes_list:
    if like['category'] in ['Food/Beverages', 'Restaurant/Cafe', 'Bar']:
        food_likes.append(like)
        like_id = like['id']
        like_object = graph.get_object(id = like_id)
        # print like_object
        if 'category_list' in like_object:
            liked_categories.append(like_object['category_list'])

liked_categories = [item['name'] for sublist in liked_categories for item in sublist]
# print food_likes
# print liked_categories




"""get location"""
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    session = rauth.OAuth1Session(**creds)


f = urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
lat = location['latitude']
lon = location['longitude']


def is_a_match(category, fb_likes):
    # print category
    # print fb_likes
    for like in fb_likes:
        if category[0].lower() in like.lower():
            return True
    return False




if time == "lunchTime":

    # ask yelp for restaurats near your location
    params = get_search_parameters(lat, lon)

    request = session.get("http://api.yelp.com/v2/search", params=params)
    data = request.json()
    session.close()

    # compare restaurants from yelp with fb interests

    recommended = []
    other = []

    for restaurant in data['businesses']:

        name = restaurant['name']
        rating = restaurant['rating']
        distance = restaurant['distance']
        #phone = restaurant['phone']

        categories = restaurant['categories']

        # print name, rating, int(distance), categories#, phone

        for category in categories:


            if is_a_match(category, liked_categories):

                recommended.append((name, rating, int(distance), categories))
            else:
                other.append((name, rating, int(distance), categories))




    i = 0

    for restaurant in recommended:
        if i<3:
            print restaurant
            i += 1
        else:
            break

    for restaurant in other:
        if i < 3:
            print restaurant
            i += 1
        else:
            break


    #TODO scarlet: send recomendations
