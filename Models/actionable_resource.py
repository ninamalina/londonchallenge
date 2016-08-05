import uuid


class ActionableResource:

    def __init__(self, description_list, actions):
        self.description_list = description_list
        self.actions = actions

    def to_json(self):
        return {
            'DescriptionList': self.description_list,
            'ActionList': [action.to_json() for action in self.actions],
            '$type': 'ActionableResource_22',
            'Id': str(uuid.uuid4())
        }
