import json
import requests

import config
from API.authorization import access_token


def create_card(to_user_email, title, content, attachment_names_ids=None):
    """

    :param to_user_email:
    :param title:
    :param content:
    :param attachment_names_ids: tuple: (name, id)
    :return:
    """
    data = {
            'Name': title,
            'Text': content,
            'ShareList': [
                {
                    '$type': 'User_14',
                    'AccountList': [
                        {
                            '$type': 'AccountEmail_14',
                            'Email': to_user_email
                        }
                    ]
                }
            ]
        }
    if attachment_names_ids:
        data['Files'] = [
                {
                    '$type': 'File_14',
                    'Id': attachment_id,
                    'Name': attachment_name
                } for attachment_name, attachment_id in attachment_names_ids
            ]

    url = '{}/post'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response

def create_card_with_impersonation(to_user_email, title, content, user_id, attachment_names_ids=None):
    """

    :param to_user_email:
    :param title:
    :param content:
    :param attachment_names_ids: tuple: (name, id)
    :return:
    """
    data = {
            'Name': title,
            'Text': content,
            'ShareList': [
                {
                    '$type': 'User_14',
                    'AccountList': [
                        {
                            '$type': 'AccountEmail_14',
                            'Email': to_user_email
                        }
                    ]
                }
            ]
        }
    if attachment_names_ids:
        data['Files'] = [
                {
                    '$type': 'File_14',
                    'Id': attachment_id,
                    'Name': attachment_name
                } for attachment_name, attachment_id in attachment_names_ids
            ]

    url = '{}/post'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token,
            'X-Impersonate-User': user_id
        },
        data=json.dumps(data)
    )

    return response


def post_to_existing_card(card_id, content, attachment_names_ids=None):
    data = {
        'Parent': {
            'Id': card_id
        },
        'Text': content
    }

    if attachment_names_ids:
        data['Files'] = [
                {
                    '$type': 'File_14',
                    'Id': attachment_id,
                    'Name': attachment_name
                } for attachment_name, attachment_id in attachment_names_ids
            ]

    url = '{}/post'.format(config.API_4O['URL'])
    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )
    return response


def create_card_html(to_user_email, title, html_content, attachment_ids=None, inline_attachment_ids=None):
    """

    :param to_user_email:
    :param title:
    :param html_content:
    :param attachment_ids: tuple: (name, id)
    :param inline_attachment_ids: tuple: (name, id)
    :return:
    """

    data = {
        'Name': title,
        'BodyHtml': html_content,
        'ShareList': [
            {
                '$type': 'User_14',
                'AccountList': [
                    {
                        '$type': 'AccountEmail_14',
                        'Email': to_user_email
                    }
                ]
            }
        ]
    }

    if attachment_ids is not None or inline_attachment_ids is not None:
        data['Files'] = []

    if attachment_ids:
        attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name
            } for attachment_name, attachment_id in attachment_ids
            ]
        data['Files'] += attachments

    if inline_attachment_ids:
        inline_attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name,
                'Hidden': True
            } for attachment_name, attachment_id in inline_attachment_ids
            ]
        data['Files'] += inline_attachments

    url = '{}/post'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response


def post_to_existing_card_html(card_id, html_content, attachment_ids=None, inline_attachment_ids=None):
    """

    :param to_user_email:
    :param title:
    :param html_content:
    :param attachment_names_ids: tuple: (name, id)
    :param attachment_ids: tuple: (name, id)
    :param inline_attachment_ids: tuple: (name, id)
    :return:
    """

    data = {
        'Parent': {
            'Id': card_id
        },
        'BodyHtml': html_content
    }

    if attachment_ids is not None or inline_attachment_ids is not None:
        data['Files'] = []

    if attachment_ids:
        attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name
            } for attachment_name, attachment_id in attachment_ids
            ]
        data['Files'] += attachments

    if inline_attachment_ids:
        inline_attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name,
                'Hidden': True
            } for attachment_name, attachment_id in inline_attachment_ids
            ]
        data['Files'] += inline_attachments

    url = '{}/post'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response


def post_attachment(document_name, document_path):
    with open(document_path, 'rb') as file:
        document = file.read()

    url = '{}/document'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Accept': 'application/vnd.4thoffice.document-v4.0+json',
            'Content-Type': 'application/octet-stream',
            'X-Upload-File-Name': document_name,
            'Authorization': access_token
        },
        data=document
    )

    return response


def get_user_chat_id(user_email):
    url = '{}/stream'.format(config.API_4O['URL'])

    data = {
        'User': {
            '$type': 'User_14',
            'AccountList': [{
                '$type': 'AccountEmail_14',
                'Email': user_email
            }]
        }
    }

    response = requests.post(
        url=url,
        headers={
            'Accept': 'application/vnd.4thoffice.stream.user-5.3+json',
            'Content-Type': 'application/vnd.4thoffice.stream.user-5.3+json',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response
