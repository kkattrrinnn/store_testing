from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class CartCheckoutPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)
        self.TEXT_DESCRIPTION = browser.find_element(By.XPATH, "//td[@class='products']")
        self.TEXT_PRICE = browser.find_element(By.XPATH, "//span[@class='uc-price']")
        self.BUTTON_SEND_ORDER = browser.find_element(By.XPATH, "//input[@id='edit-continue']")

    def GetPriceInt(self):
        temp_list = self.TEXT_PRICE.text.split()
        price_int = temp_list[0]
        return price_int

    def GetArticleInt(self):
        temp_list = self.TEXT_DESCRIPTION.text.split()
        article_int = temp_list[0]
        return article_int

    def ClickButtonSendOrder(self):
        self.BUTTON_SEND_ORDER.click()