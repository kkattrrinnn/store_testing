import pytest

from constants.urls import Backend
from tools.api.requests_api import RequestsApi


class TestCRUD:

    def test_create_object(self):
        requests_api = RequestsApi(Backend.BASE_URL)
        pytest.requests_api = requests_api

        payload = {
           "name": "Apple MacBook Pro 16",
           "data": {
              "year": 2019,
              "price": 1849.99,
              "CPU model": "Intel Core i9",
              "Hard disk size": "1 TB"
           }
        }
        response = requests_api.Post(Backend.CREATE_ENDPOINT, payload).json()
        pytest.response = response
        assert response["id"] != 0

    def test_read_object(self):
        requests_api = RequestsApi(Backend.BASE_URL)
        pytest.requests_api = requests_api

        response = requests_api.Get(f"{Backend.READ_ENDPOINT}/{pytest.response['id']}").json()
        assert response["id"] == pytest.response["id"]

    def test_update_object(self):
        requests_api = RequestsApi(Backend.BASE_URL)
        pytest.requests_api = requests_api

        new_value = 3000
        payload = {
           "name": "Apple MacBook Pro 16",
           "data": {
              "year": new_value,
              "price": 1849.99,
              "CPU model": "Intel Core i9",
              "Hard disk size": "1 TB"
           }
        }
        response = requests_api.Put(f"{Backend.UPDATE_ENDPOINT}/{pytest.response['id']}", payload).json()
        assert response["id"] == pytest.response["id"]
        assert int(response["data"]["year"]) == new_value

    def test_delete_object(self):
        requests_api = RequestsApi(Backend.BASE_URL)
        pytest.requests_api = requests_api

        response_delete = requests_api.Delete(f"{Backend.DELETE_ENDPOINT}/{pytest.response['id']}")
        response_get = requests_api.Get(f"{Backend.READ_ENDPOINT}/{pytest.response['id']}")
        assert response_get.status_code == 404
