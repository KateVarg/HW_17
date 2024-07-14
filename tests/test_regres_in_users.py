import requests
from jsonschema import validate
from schemas.user import get_user, post_user, put_user


endpoint_user = '/users/'


def test_get_single_user(base_url):
    id_user = 4
    response = requests.get(base_url + endpoint_user + str(id_user))

    assert response.status_code == 200
    assert response.json()['data']['id'] == id_user
    validate(response.json(), get_user)


def test_post_create_user(base_url):
    payload = {
        "name": "Jhon",
        "job": "team-leader"
    }
    response = requests.post(base_url + endpoint_user, data=payload)

    assert response.status_code == 201
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']
    validate(response.json(), post_user)


def test_put_user(base_url):
    id_user = 4
    payload = {
        "name": "Mark",
        "job": "team-leader"
    }
    response = requests.put(base_url + endpoint_user + str(id_user), data=payload)

    assert response.status_code == 200
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']
    validate(response.json(), put_user)


def test_delete_user(base_url):
    id_user = 4
    response = requests.delete(base_url + endpoint_user + str(id_user))

    assert response.status_code == 204
    assert response.text == ''
