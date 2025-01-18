from selenium import webdriver
from selenium.webdriver.common.by import By


class Page:
    def __init__(self, driver : webdriver):
        self.DRIVER = driver

