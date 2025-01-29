import pytest


def pytest_configure():
    pytest.requests_api = None
    pytest.response = None

@pytest.fixture(autouse=True)
def CloseSession(request):
    def finalizer():
        pytest.requests_api.Close_Session()
    request.addfinalizer(finalizer)