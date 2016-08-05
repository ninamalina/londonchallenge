import json
import os

from API.card import create_card, post_to_existing_card, post_attachment, get_user_chat_id, create_card_html, \
    post_to_existing_card_html, create_card_with_impersonation
from API.get_data import get_user_by_email, get_stream, get_group, get_streams_of_user, get_cards_of_stream, \
    get_chat_messages, get_messages_of_a_card
from API.push_notification import send_push_notification
from Models.user import User
from Models.group import Group

def example_send_push_notification(user):

    push_notification_message = 'Hi {}, check what I found for you'.format(user.first_name)
    custom_id = 'Notification.example'
    response = send_push_notification(user.id, custom_id, push_notification_message)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_user_by_email(user_email):
    response = get_user_by_email(user_email)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_new_card(user):
    title = 'Welcome!'
    content = 'Hello {}, this is me, your smart assistant'.format(user.first_name)

    response = create_card(user.email, title, content)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_new_card_with_impersonation(user, user_to_impersonate_id):
    title = 'Welcome!'
    content = 'Hello {}, this is an impersonated message'.format(user.first_name)

    response = create_card_with_impersonation(user.email, title, content, user_to_impersonate_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_to_existing_card(user):
    data = example_post_new_card(user)
    card_id = data['Parent']['Id']
    content = 'One more thing, {}'.format(user.first_name)
    response = post_to_existing_card(card_id, content)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_with_attachment(user):
    title = 'Welcome with attachment!'
    content = 'Hello {}, this is me, your smart assistant'.format(user.first_name)
    file_name = '4thOffice.png'
    document_path = '{}{}{}'.format(os.path.dirname(os.path.abspath(__file__)), os.sep, file_name)
    response = post_attachment(file_name, document_path)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    attachment_id = json.loads(response.text)['Id']
    attachment_names_ids = [(file_name, attachment_id)]

    response = create_card(user.email, title, content, attachment_names_ids)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_chat_message(user):
    response = get_user_chat_id(user.email)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    card_chat_id = data['Id']

    content = 'Hi {}, this is a chat message ;)'.format(user.name)
    response = post_to_existing_card(card_chat_id, content)
    return response


def example_get_stream(user_id, stream_id):
    response = get_stream(user_id, stream_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_group(user_id, group_id):
    response = get_group(user_id, group_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_streams_of_user(user):
    response = get_streams_of_user(user.id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    frist_stream_id = data['MenuItemList'][0]['Resource']['Id']
    return frist_stream_id


def example_get_groups_of_user(user):
    response = get_streams_of_user(user.id, group_streams_only=True)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    frist_stream_id = data['MenuItemList'][0]['Resource']['Id']
    return frist_stream_id


def example_post_new_card_html(user):
    title = 'Welcome!'

    file_name = '4thOffice.png'
    document_path = '{}{}{}'.format(os.path.dirname(os.path.abspath(__file__)), os.sep, file_name)
    response = post_attachment(file_name, document_path)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    attachment_id = json.loads(response.text)['Id']
    inline_attachment_names_ids = [(file_name, attachment_id)]

    content = '<html><head><title>Title</title></head><body><b>test with image</b><br />' \
              '<img src="cid:{}" /></body></html>'.format(attachment_id)

    response = create_card_html(user.email, title, content, inline_attachment_ids=inline_attachment_names_ids)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_to_existing_card_html(user):
    data = example_post_new_card(user)
    card_id = data['Parent']['Id']
    file_name = '4thOffice.png'
    document_path = '{}{}{}'.format(os.path.dirname(os.path.abspath(__file__)), os.sep, file_name)
    response = post_attachment(file_name, document_path)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    attachment_id = json.loads(response.text)['Id']
    inline_attachment_names_ids = [(file_name, attachment_id)]

    content = '<html><head><title>Title</title></head><body><b>test with image</b><br />' \
              '<img src="cid:{}" /></body></html>'.format(attachment_id)
    response = post_to_existing_card_html(card_id, content, inline_attachment_ids=inline_attachment_names_ids)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_cards_of_stream(user):
    stream_id = example_get_streams_of_user(user)
    response = get_cards_of_stream(user.id, stream_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_messages_of_a_card(user):
    data = example_get_cards_of_stream(user)
    first_card_id = data['DiscussionListPage']['DiscussionList'][0]['Id']
    response = get_messages_of_a_card(user.id, first_card_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_chat_messages(user):
    response = get_user_chat_id(user.email)
    data = json.loads(response.text)
    chat_id = data['Id']

    response = get_chat_messages(user.id, chat_id, size=10)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data

user_email = 'gregor.kuznik@gmail.com'
print(example_get_user_by_email(user_email))
user = User(example_get_user_by_email(user_email))
group_id = example_get_groups_of_user(user)
group = Group(example_get_group(user.id, group_id))
print(group)
#result = example_send_push_notification(user)
#result = example_post_new_card_with_impersonation(user, user.id)
#print(result)