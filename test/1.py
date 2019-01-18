from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import socket
import ssl
from OpenSSL import crypto
from requests import Session
from requests_pkcs12 import Pkcs12Adapter


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("https://ga-s3-new.russian-lotteries.net/")
        passwd="114b86f9c4"
        # open it, using password. Supply/read your own from stdin.
        p12 = crypto.load_pkcs12(open("C:\\PycharmProjects\\S3\\2000006809.p12", 'rb').read(), passwd)

        # get various properties of said file.
        # note these are PyOpenSSL objects, not strings although you
        # can convert them to PEM-encoded strings.
        p12.get_certificate()  # (signed) certificate object
        p12.get_privatekey()  # private key.
        p12.get_ca_certificates()  # ca chain.


        #with Session() as s:
        #   s.mount('https://ga-s3-new.russian-lotteries.net/',
        #            Pkcs12Adapter(pkcs12_filename='C:\\PycharmProjects\\S3\\2000006809.p12', pkcs12_password='114b86f9c4'))
        #    r = s.get('https://ga-s3-new.russian-lotteries.net/login')

        



        wd.find_element_by_name("username").send_keys("20003510")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("34756381")
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()
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