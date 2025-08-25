import os
from dotenv import load_dotenv
from dotenv import set_key
import requests
import pytest
from core.headers import Headers
load_dotenv()

# Только если запуск локальная перезаписать .env 
@pytest.fixture(scope='session', autouse=True)
def init_tokens():
    response = requests.post(
        url=f"{os.getenv('HOST')}/auth/refresh/",
        json = {'refresh_token': os.getenv('REFRESH_TOKEN')}
    )
    assert response.status_code == 200, f"Failed requests {response.text}"

    access_token = response.json().get('tokens', {}).get('access', {}).get('token')
    refresh_token = response.json().get('tokens', {}).get('refresh', {}).get('token')
    set_key(".env", "ACCESS_TOKEN", access_token)
    set_key(".env", "REFRESH_TOKEN", refresh_token)
    return response


@pytest.fixture()
def get_currency_id():
    headers = Headers().basic
    response = requests.get(
        url = f"{os.getenv('HOST')}/currencies/",
        headers=headers
    )
    assert response.status_code == 200, f"Failed requests {response.text}"

    currencies = response.json()
    cur_usd = next((c for c in currencies if c.get('code') == 'EUR'), None)
    assert cur_usd is not None, f"Currency with code 'EUR' not found"
    return cur_usd['id']