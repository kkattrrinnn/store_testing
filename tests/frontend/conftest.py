import pytest
from tools.frontend.driver import Driver


driver = None


@pytest.fixture(autouse=False)
def create_driver():
    global driver
    driver = Driver()
    return driver


@pytest.fixture(autouse=False)
def get_driver():
    global driver
    return driver


@pytest.fixture(autouse=False)
def destroy_driver(request):
    global driver

    def finalizer():
        driver.Close()

    request.addfinalizer(finalizer)