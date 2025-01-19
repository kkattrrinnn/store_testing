from selenium import webdriver


class Driver:
    def __init__(self):
        self.BROWSER = webdriver.Safari()
        self.BROWSER.maximize_window()

    def OpenPage(self, url):
        self.BROWSER.get(url)

    def RefreshPage(self):
        self.BROWSER.refresh()

    def Close(self):
        self.BROWSER.close()

    def DeleteCookies(self):
        self.BROWSER.delete_all_cookies()
        self.RefreshPage()

    def GetCurrentURL(self):
        return self.BROWSER.current_url