import pytest
from tools.frontend.pages.driver import Driver


@pytest.fixture(autouse=True)
def create_driver(request):

    def finalizer():
        driver.BROWSER.close()

    request.addfinalizer(finalizer)

    driver = Driver()
    return driver