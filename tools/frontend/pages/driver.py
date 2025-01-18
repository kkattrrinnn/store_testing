from selenium import webdriver


class Driver:
    def __init__(self):
        self.BROWSER = webdriver.Safari()
        self.BROWSER.maximize_window()

    def OpenPage(self, url):
        self.BROWSER.get(url)

    def Close(self):
        self.BROWSER.close()