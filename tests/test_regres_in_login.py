import requests
import json
from jsonschema import validate


def test_post_login_success(base_url, endpoint_login):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(base_url + endpoint_login, data=payload)

    assert response.status_code == 200
    assert response.json()['token']
    with open('schemas/login.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_post_login_fail(base_url, endpoint_login):
    payload = {
        "email": "peter@klaven"
    }
    response = requests.post(base_url + endpoint_login, data=payload)

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"
