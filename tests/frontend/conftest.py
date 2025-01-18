import pytest
from tools.frontend.pages.driver import Driver


@pytest.fixture(autouse=True)
def create_driver():
    driver = Driver()
    return driver


@pytest.fixture(autouse=True)
def destroy_driver(create_driver):
    yield
    create_driver.BROWSER.close()
