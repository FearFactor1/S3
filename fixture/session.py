


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()
        wd.get_screenshot_as_file('C:\PycharmProjects\S3\screen\session\\login.png')


    def exit_s3(self):
        wd = self.app.wd
        # click to exit s3
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='«Моментальные»'])[1]/following::span[2]").click()
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Очистить временные данные?'])[1]/following::button[1]").click()
        wd.get_screenshot_as_file('C:\PycharmProjects\S3\screen\session\\exit_s3.png')

