import pytest
from constants.urls import Frontend
from tools.frontend.fake_data import FakeData
from tools.frontend.pages.initial_page import InitialPage

class TestAuthorization:

    @pytest.mark.usefixtures
    @pytest.mark.parametrize("login, password",
                             [("620000ekb@gmail.com", "qwerty123")])
    def test_valid_data(self, create_driver, login, password):
        create_driver.OpenPage(Frontend.MAIN_PAGE)
        main_page = InitialPage(create_driver.BROWSER)
        
        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfAuthorizationPassed() == True

    @pytest.mark.usefixtures
    @pytest.mark.parametrize("login, password",
                             [(FakeData.GetFakeEmail(), FakeData.GetRandomPassword()),
                              (FakeData.GetFakeEmail(), FakeData.GetRandomPassword())])
    def test_invalid_data(self, get_driver, login, password):
        get_driver.DeleteCookies()
        get_driver.OpenPage(Frontend.MAIN_PAGE)
        main_page = InitialPage(get_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfDataInFieldsIsInvalid() == True

    @pytest.mark.usefixtures
    @pytest.mark.parametrize("login, password",
                             [("", FakeData.GetRandomPassword()), ("", FakeData.GetRandomPassword())])
    def test_empty_login_input(self, get_driver, login, password):
        get_driver.DeleteCookies()
        main_page = InitialPage(get_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfDataInFieldsIsInvalid() == True

    @pytest.mark.usefixtures
    @pytest.mark.parametrize("login, password",
                             [(FakeData.GetFakeEmail(), ""), (FakeData.GetFakeEmail(), "")])
    def test_empty_password_input(self, get_driver, login, password):
        get_driver.DeleteCookies()
        main_page = InitialPage(get_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfDataInFieldsIsInvalid() == True

    @pytest.mark.usefixtures
    @pytest.mark.parametrize("login, password", [("", "")])
    def test_empty_login_password_inputs(self, get_driver, destroy_driver, login, password):
        get_driver.DeleteCookies()
        main_page = InitialPage(get_driver.BROWSER)

        main_page.SetupInputLogin(login)
        main_page.SetupInputPassword(password)
        main_page.ClickButtonLogin()

        assert main_page.CheckIfDataInFieldsIsInvalid() == True

