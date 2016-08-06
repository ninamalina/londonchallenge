import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAIXOt5mzpmrQoWecbZC2hDgEM4OlUl38fXfSpeXZB2FAUs54lxMiZAijpBM0p1Dtn97zyb76A041zMO1CPR3TIeeMSfLG426GZBCl5fDHfB1YMTFq7NaYCw0zy9Q1AS72ke0704iIiWk4kJrZC9xnv6of0ovZBxAZDZD', version='2.2');
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
for like in likes_list:
    if like['category'] == 'Food/Beverages':
        food_likes.append(like)
#friends = graph.get_connections(user["id"], "friends")

