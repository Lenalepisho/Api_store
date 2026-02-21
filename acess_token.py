import request
from requests.auth import HTTPBasicAuth
from django.conf import settings


def generate_access_token():
    res=request.get(settings.ACCESS_TOKEN_URL,auth=HTTPBasicAuth(settings.CONSUMER_KEY,settings.CONSUMER_SECRETE))

    json_res=res.json()
    access_token=json_res['access_token']
    """
    Generate an access token using client credentials.

    Args:
        client_id (str): The client ID.
        client_secret (str): The client secret.
        token_url (str): The URL to obtain the access token.

    Returns:
        str: The access token.
    """
    response = request.get(
        token_url,
        auth=HTTPBasicAuth(client_id, client_secret),
        data={'grant_type': 'client_credentials'}
    )

    if response.status_code == 200:
        token_data = response.json()
        return token_data.get('access_token')
    else:
        raise Exception(f"Failed to obtain access token: {response.status_code} - {response.text}")