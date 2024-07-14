import requests
import json
from jsonschema import validate
import re

endpoint_login = '/login'


def test_post_login_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(base_url + endpoint_login, data=payload)
    token = response.json().get("token")
    token_pattern = r"^[A-Za-z0-9]+$"

    assert response.status_code == 200
    assert re.match(token_pattern, token)

    with open('schemas/login.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_post_login_fail(base_url):
    payload = {
        "email": "peter@klaven"
    }
    response = requests.post(base_url + endpoint_login, data=payload)

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"
