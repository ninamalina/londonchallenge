class Group:
    def __init__(self, group_json_object):
        self.id = group_json_object['Id']
        self.name = group_json_object['Name']
        self.member_count = group_json_object['MemberCount']
        self.email = group_json_object['Email']
        self.members = group_json_object['Members']
        self.description = group_json_object['Description']
