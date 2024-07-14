import requests
import json
from jsonschema import validate


endpoint_register = '/register'


def test_post_register_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(base_url + endpoint_register, data=payload)

    assert response.status_code == 200
    with open('schemas/register.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_post_register_fail(base_url):
    payload = {
        "email": "sydney@fife"
    }
    response = requests.post(base_url + endpoint_register, data=payload)

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"
