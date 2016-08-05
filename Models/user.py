class User:
    def __init__(self, user_json_object):
        self.id = user_json_object['Id']
        self.name = user_json_object['Name']
        self.first_name = user_json_object['FirstName']
        self.last_name = user_json_object['LastName']
        self.email = user_json_object['AccountList'][0]['Email']
