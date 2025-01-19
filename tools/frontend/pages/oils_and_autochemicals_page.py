from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class OilsAndAutochemicalsPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)
        self.BUTTON_BMW = browser.find_element(By.XPATH, "//a[@title='BMW']")

    def ClickButtonBMW(self):
        self.BUTTON_BMW.click()