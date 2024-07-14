import requests
import json
from jsonschema import validate


endpoint_login = '/login'


def test_post_login_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(base_url + endpoint_login, data=payload)

    assert response.status_code == 200
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
