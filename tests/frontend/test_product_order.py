import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.urls import Frontend
from tests.frontend.test_authorization import TestAuthorization
from tools.frontend.pages.bmw_page import BMWPage
from tools.frontend.pages.cart_checkout_page import CartCheckoutPage
from tools.frontend.pages.cart_page import CartPage
from tools.frontend.pages.initial_page import InitialPage
from tools.frontend.pages.main_page import MainPage
from tools.frontend.pages.oils_and_autochemicals_page import OilsAndAutochemicalsPage

"""flow : open catalog -> add product to cart -> place order"""
class TestProductOrder:

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
    def test_add_product_to_cart(self, get_driver):
        browser = get_driver.BROWSER

        # go to "oils and autochemicals" catalogue
        main_page = MainPage(browser)
        main_page.Click_Button_Oils_And_Autochemicals()
        url_changed_to_desired = (WebDriverWait(browser, 10).until
                                 (expected_conditions.url_to_be(Frontend.OILS_AND_AUTOCHEMICALS_PAGE)))
        assert url_changed_to_desired == True

        # go to "BMW" catalogue
        oils_and_autochemicals_page = OilsAndAutochemicalsPage(browser)
        oils_and_autochemicals_page.ClickButtonBMW()
        url_changed_to_desired = (WebDriverWait(browser, 10).until
                                 (expected_conditions.url_to_be(Frontend.BMW_OILS_AND_AUTOCHEMICALS_PAGE)))
        assert url_changed_to_desired == True

        # add first product to cart
        bmw_page = BMWPage(browser)
        current_price = bmw_page.GetPriceInt()
        current_article = bmw_page.GetArticleInt()
        bmw_page.ClickButtonAddToCart()

        url_changed_to_desired = (WebDriverWait(browser, 10).until
                                 (expected_conditions.url_to_be(Frontend.CART_PAGE)))
        assert url_changed_to_desired == True

        # check if price is actual
        cart_page = CartPage(browser)
        assert cart_page.GetPriceInt() == current_price

        # check if article is actual
        assert cart_page.GetArticleInt() == current_article

        # place an order
        cart_page.CLickButtonPlaceOrder()
        url_changed_to_desired = (WebDriverWait(browser, 10).until
                                 (expected_conditions.url_to_be(Frontend.CART_CHECKOUT_PAGE)))
        assert url_changed_to_desired == True

        # send the order
        cart_checkout_page = CartCheckoutPage(browser)
        cart_checkout_page.ClickButtonSendOrder()
        url_changed_to_desired = (WebDriverWait(browser, 10).until
                                 (expected_conditions.url_to_be(Frontend.ORDER_COMPLETE)))
        assert url_changed_to_desired == True