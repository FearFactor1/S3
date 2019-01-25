# Тест: Кнопка Войти не доступна после кликов на поле логин и пароль
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest



class TestInvisibleButton(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def test_invisible_button(self):
        self.login_invisible_button() # проверка, что кнопка Войти не доступна


    def login_invisible_button(self):
        wd = self.wd
        # клик на поле логин и пароль, проверка, что поле Войти не доступна
        self.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_xpath("(//input[@disabled='disabled'])")


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:9999")


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()