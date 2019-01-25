from selenium.webdriver.firefox.webdriver import WebDriver
import unittest



class TestReportToday(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_report_today(self):
        wd = self.wd
        self.login(wd, username="20003510", password="34756381")
        self.report_today(wd)
        self.exit_s3(wd)


    def exit_s3(self, wd):
        # click to exit s3
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='«Моментальные»'])[1]/following::span[2]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Очистить временные данные?'])[1]/following::button[1]").click()


    def report_today(self, wd):
        self.open_home_page(wd)
        # click to report
        wd.find_element_by_link_text(u"Отчёты").click()
        # click to button report
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кассовый отчет'])[1]/following::button[1]").click()
        # click comeback
        wd.find_element_by_link_text(u"Назад").click()
        # click close modal window
        wd.find_element_by_css_selector("div.modal__body-close").click()


    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()


    def open_home_page(self, wd):
        wd.get("http://localhost:9999")


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()