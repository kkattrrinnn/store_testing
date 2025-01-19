from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class MainPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)

        button_enabled = (WebDriverWait(self.BROWSER, 10).until
        (expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@class='menu']/li[5]/a/span"))))
        self.BUTTON_OILS_AND_AUTOCHEMICALS = browser.find_element(By.XPATH, "//ul[@class='menu']/li[5]/a/span")

    def Click_Button_Oils_And_Autochemicals(self):
        self.BUTTON_OILS_AND_AUTOCHEMICALS.click()

