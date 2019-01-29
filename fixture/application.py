from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.login import LoginHelper
from fixture.report import ReportHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(7)
        self.session = SessionHelper(self)
        self.login = LoginHelper(self)
        self.report = ReportHelper(self)





    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:9999")


    def destroy(self):
        self.wd.quit()