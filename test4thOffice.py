import json

from API.get_data import get_user_by_email
from Models.user import User


def example_get_user_by_email(user_email):
    response = get_user_by_email(user_email)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data

user_email = 'gregor.kuznik@gmail.com'
user = User(example_get_user_by_email(user_email))
print(user.first_name)