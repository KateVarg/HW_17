import requests
import json
from jsonschema import validate


def test_post_register_success(base_url, endpoint_register):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(base_url + endpoint_register, data=payload)

    assert response.status_code == 200
    assert response.json()['id']
    with open('schemas/register.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_post_register_fail(base_url, endpoint_register):
    payload = {
        "email": "sydney@fife"
    }
    response = requests.post(base_url + endpoint_register, data=payload)

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"
