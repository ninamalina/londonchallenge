import json
import requests
import config

def login():
    endpoint = '{0}/{1}'.format(config.API_4O['URL'], 'user/session/logon')

    response = requests.post(
        endpoint,
        headers={
            'Accept': 'application/vnd.4thoffice.logon.user-v4.0+json',
            'Content-Type': 'application/vnd.4thoffice.logon.user-v4.0+json'
        },
        data=json.dumps({
            "Authentication": {
                "AuthenticationType": 7,
                "AuthenticationId": config.SMART_ASSISTANT['AUTH']['KEY'],
                "AuthenticationToken": config.SMART_ASSISTANT['AUTH']['SECRET']
            },
            "ClientApplication": {
                "Type": 0,
                "Version": "0.1",
                "CodeName": "Bots"
            }
        })
    )

    if response.status_code != 200:
        response.raise_for_status()

    data = json.loads(response.text)
    return 'Bearer ' + data['Token']['AccessToken']


access_token = None

if not access_token:
    print('Getting access token...')
    access_token = login()
