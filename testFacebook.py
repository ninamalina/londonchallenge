import facebook

graph = facebook.GraphAPI(access_token='#token#', version='2.2');
user = graph.get_object("me")
print(user)
friends = graph.get_connections(user["id"], "friends")
print(friends)