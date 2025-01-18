import pytest
from constants.urls import Frontend
from tools.frontend.fake_data import FakeData
from tools.frontend.pages.main_page import MainPage


class TestAuthorization:

    @pytest.mark.parametrize("login, password",
                             [("620000ekb@gmail.com", "qwerty123")])
    def test_valid_data(self, create_driver, login, password):
        create_driver.OpenPage(Frontend.MAIN_PAGE)
        main_page = MainPage(create_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfAuthorizationPassed() == True

    @pytest.mark.parametrize("login, password",
                             [(FakeData.GetFakeEmail(), FakeData.GetRandomPassword()),
                              (FakeData.GetFakeEmail(), FakeData.GetRandomPassword())])
    def test_invalid_data(self, create_driver, login, password):
        create_driver.OpenPage(Frontend.MAIN_PAGE)
        main_page = MainPage(create_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfDataInFieldsIsInvalid() == True

    @pytest.mark.parametrize("login, password",
                             [("", FakeData.GetRandomPassword()), ("", FakeData.GetRandomPassword())])
    def test_empty_login_input(self, create_driver, login, password):
        pass

    @pytest.mark.parametrize("login, password",
                             [(FakeData.GetFakeEmail(), ""), (FakeData.GetFakeEmail(), "")])
    def test_empty_password_input(self, create_driver, login, password):
        pass

    @pytest.mark.parametrize("login, password", [("", "")])
    def test_empty_login_password_inputs(self, create_driver, login, password):
        pass


