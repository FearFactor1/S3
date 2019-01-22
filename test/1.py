from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost:9999")
        wd.find_element_by_name("username").send_keys("20003510")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("34756381")
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()
        wd.find_element_by_link_text(u"Отчёты").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кассовый отчет'])[1]/following::button[1]").click()
        wd.find_element_by_link_text(u"Назад").click()
        wd.find_element_by_css_selector("div.modal__body-close").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='«Моментальные»'])[1]/following::span[2]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Очистить временные данные?'])[1]/following::button[1]").click()


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