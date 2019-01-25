from selenium.webdriver.firefox.webdriver import WebDriver
import unittest



class TestScreenKeyboard(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_screen_keyboard(self):
        wd = self.wd
        self.login_keyboard(wd)
        self.exit_s3(wd)


    def exit_s3(self, wd):
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='«Моментальные»'])[1]/following::span[2]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Очистить временные данные?'])[1]/following::button[1]").click()


    def login_keyboard(self, wd):
        # press login and password on keyboard
        self.open_home_page(wd)
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("")
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("")
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_css_selector("span.icon.icon-keyboard.modal-link-local").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[3]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::div[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::div[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::div[1]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[4]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[6]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[2]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::div[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::button[1]").click()
        wd.find_element_by_css_selector(
            "span.icon.icon-keyboard.modal-link-local.modal-link-local_password").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[4]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[5]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[8]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[6]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[7]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[4]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[9]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Введите число'])[1]/following::div[2]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='C'])[1]/following::button[1]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Представьтесь, кто вы?'])[1]/following::input[4]").click()


    def open_home_page(self, wd):
        wd.get("http://localhost:9999")


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()