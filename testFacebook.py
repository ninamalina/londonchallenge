import facebook

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
categories = []

for like in likes_list:
    if like['category'] in ['Food/Beverages', 'Restaurant/Cafe', 'Bar']:
        food_likes.append(like)
        like_id = like['id']
        like_object = graph.get_object(id = like_id)
        print like_object
        if 'category_list' in like_object:
            categories.append(like_object['category_list'])


print food_likes
print categories

#friends = graph.get_connections(user["id"], "friends")

