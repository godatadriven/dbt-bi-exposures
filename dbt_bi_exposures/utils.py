import requests
from requests.exceptions import HTTPError
from typing import Dict

def get_request_handler(url: str) -> Dict:
    """
    Request handler method

    Params
    ------
    url : str
        Url endpoint to make the request to
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    except HTTPError as http_err:
        raise
    except Exception as err:
        raise