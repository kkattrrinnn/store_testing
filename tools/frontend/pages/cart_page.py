from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class CartPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)

        button_enabled = (WebDriverWait(self.BROWSER, 10).until
                          (expected_conditions.presence_of_element_located(
                              (By.XPATH, "//input[@id='edit-checkout']"))))
        self.BUTTON_PLACE_ORDER = browser.find_element(By.XPATH, "//input[@id='edit-checkout']")

        self.TEXT_PRICE = browser.find_element(By.XPATH, "//td[@class='desc']/div[3]")
        self.NAME_OF_PRODUCT = browser.find_element(By.XPATH, "//td[@class='desc']/div")

    def GetPriceInt(self):
        temp_list = self.TEXT_PRICE.text.split()
        price_int = temp_list[0]
        return price_int

    def GetArticleInt(self):
        temp_list = self.NAME_OF_PRODUCT.text.split()
        article_int = temp_list[0]
        return article_int

    def CLickButtonPlaceOrder(self):
        self.BUTTON_PLACE_ORDER.click()