from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class BMWPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)

        button_enabled = (WebDriverWait(self.BROWSER, 10).until
        (expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='edit-submit-2800808']"))))
        self.BUTTON_ADD_TO_CART = browser.find_element(By.XPATH, "//input[@id='edit-submit-2800808']")

        self.TEXT_PRICE = browser.find_element(By.XPATH, "//tr[@class='odd']/td/div[@class='bbprice']")
        self.NAME_OF_PRODUCT = browser.find_element(By.XPATH, "//div[@id='content-area']/div[2]/div[2]/p[1]")

    def GetPriceInt(self):
        temp_list = self.TEXT_PRICE.text.split()
        price_int = temp_list[0]
        return price_int

    def GetArticleInt(self):
        temp_list = self.NAME_OF_PRODUCT.text.split()
        article_int = temp_list[1]
        return article_int

    def ClickButtonAddToCart(self):
        self.BUTTON_ADD_TO_CART.click()