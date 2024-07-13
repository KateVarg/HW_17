import pytest


@pytest.fixture(autouse=True)
def base_url():
    base_url = 'https://reqres.in/api'

    return base_url


@pytest.fixture(autouse=True)
def endpoint_resource():
    endpoint_resource = '/unknown/'

    return endpoint_resource


@pytest.fixture(autouse=True)
def endpoint_user():
    endpoint_user = '/users/'

    return endpoint_user


@pytest.fixture(autouse=True)
def endpoint_register():
    endpoint_register = '/register'

    return endpoint_register


@pytest.fixture(autouse=True)
def endpoint_login():
    endpoint_login = '/login'

    return endpoint_login
