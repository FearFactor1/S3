from selenium.webdriver.firefox.webdriver import WebDriver



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(7)


    def exit_s3(self):
        wd = self.wd
        # click to exit s3
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='«Моментальные»'])[1]/following::span[2]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Очистить временные данные?'])[1]/following::button[1]").click()


    def report_today(self):
        wd = self.wd
        self.open_home_page()
        # click to report
        wd.find_element_by_link_text(u"Отчёты").click()
        # click to button report
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кассовый отчет'])[1]/following::button[1]").click()
        # click comeback
        wd.find_element_by_link_text(u"Назад").click()
        # click close modal window
        wd.find_element_by_css_selector("div.modal__body-close").click()


    def login_invisible_button(self):
        wd = self.wd
        # клик на поле логин и пароль, проверка, что поле Войти не доступна
        self.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_xpath("(//input[@disabled='disabled'])")


    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:9999")


    def destroy(self):
        self.wd.quit()