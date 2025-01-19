from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tools.frontend.pages.page import Page

class InitialPage(Page):
    def __init__(self, browser : webdriver):
        super().__init__(browser)
        self.INPUT_LOGIN = browser.find_element(By.XPATH, "//*[@id='edit-name']")
        self.INPUT_PASSWORD = browser.find_element(By.XPATH, "//*[@id='edit-pass']")
        self.BUTTON_LOGIN = browser.find_element(By.XPATH, "//*[@id='edit-submit']")

    def SetupInputLogin(self, value):
        self.INPUT_LOGIN.send_keys(value)

    def SetupInputPassword(self, value):
        self.INPUT_PASSWORD.send_keys(value)

    def ClickButtonLogin(self):
        self.BUTTON_LOGIN.click()

    def CheckIfAuthorizationPassed(self):
        expected_element_xpath = "//*[@id='block-menu-menu-site-menu_left']/div/div[1]/div/h2"
        expected_element_value = "Личный кабинет"

        desired_element_found = (WebDriverWait(self.BROWSER, 10).until
                                 (expected_conditions.text_to_be_present_in_element
                                  ((By.XPATH, expected_element_xpath), expected_element_value)))
        return desired_element_found

    def CheckIfDataInFieldsIsInvalid(self):
        expected_element_xpath = "//*[@id='block-user-0_left']/div/div[1]/div/h2"
        expected_element_value = "Вход в систему"

        desired_element_found = (WebDriverWait(self.BROWSER, 10).until
                                 (expected_conditions.text_to_be_present_in_element
                                  ((By.XPATH, expected_element_xpath), expected_element_value)))
        return desired_element_found