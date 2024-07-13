import requests
from jsonschema import validate
import json


def test_get_single_resource(base_url, endpoint_resource):
    id_user = 4
    response = requests.get(base_url + endpoint_resource + str(id_user))

    assert response.status_code == 200
    assert response.json()['data']['id'] == id_user
    with open('schemas/resource.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_get_single_resource_not_found(base_url, endpoint_resource):
    id_user = 45
    response = requests.get(base_url + endpoint_resource + str(id_user))

    assert response.status_code == 404
    assert response.json() == {}
