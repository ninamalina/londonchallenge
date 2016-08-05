import uuid

import config
from Models.actionable_resource import ActionableResource

class Action:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __call__(self):
        if self.type == 'ActionNextStep_18':
            description_list = [
                'This is static response!',
                'And here is another one!'
            ]
            actions = [
                Action(name='Great, thanks for now', type='ActionFinishWorkflow_18')
            ]
            actionable_resource = ActionableResource(description_list=description_list, actions=actions)
            return actionable_resource

        elif self.type == 'ActionFinishWorkflow_18':
            description_list = [
                'OK, see you later'
            ]
            actionable_resource = ActionableResource(description_list=description_list, actions=[])
            return actionable_resource

    def to_json(self):
        return {
            'Name': self.name,
            '$type': self.type,
            'ActionType': 'Positive',
            'Id': str(uuid.uuid4()),
            'AssistantEmail': config.SMART_ASSISTANT['AUTH']['KEY']
        }


def action_from_json(action_json):
    return Action(name=action_json['Name'], type=action_json['$type'])
