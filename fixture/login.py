


class LoginHelper:

    def __init__(self, app):
        self.app = app


    def invisible_button(self):
        wd = self.app.wd
        # клик на поле логин и пароль, проверка, что поле Войти не доступна
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_xpath("(//input[@disabled='disabled'])")
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\screen\\login\\login_invisible_button.png')
        wd.find_element_by_xpath("(//input[@type='submit'])").is_displayed()


    def press_keyboard(self):
        wd = self.app.wd
        # press login and password on keyboard
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("")
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("")
        wd.find_element_by_xpath("//body").click()
        # Прокликивание логина через экранную клавиатуру
        wd.find_element_by_css_selector("span.icon.icon-keyboard.modal-link-local").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(2)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(1)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_class_name("btn.btn_transperent.modal__prompt").click()
        wd.find_element_by_css_selector("span.icon.icon-keyboard.modal-link-local.modal-link-local_password").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(4)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(7)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(6)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(8)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(1)").click()
        wd.find_element_by_class_name("btn.btn_transperent.modal__prompt").click()
        wd.find_element_by_css_selector("div > input[value='Войти']").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\screen\\login\\login_keyboard.png')
