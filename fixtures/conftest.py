import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()

@pytest.fixture(scope='session', autouse=True)
def refresh_token():
    response = requests.post(
        url=f"{os.getenv('HOST')}/auth/refresh/",
        json = {'refresh_token': os.getenv('REFRESH_TOKEN')}
    )
    assert response.status_code == 200, f"Failed requests {response.text}"

    access_token = response.json().get('access_token')
    os.environ['ACCESS_TOKEN'] = access_token
    print(access_token)

