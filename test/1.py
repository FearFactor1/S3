from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("https://ga-s3-new.russian-lotteries.net/")
        wd.find_element_by_link_text(u"Отчёты").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кассовый отчет'])[1]/following::button[1]").click()
        wd.find_element_by_link_text(u"Назад").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()