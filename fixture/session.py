


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
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\login.png')


    def exit_s3(self):
        wd = self.app.wd
        # click to exit s3
        wd.find_element_by_class_name("icon.icon-exit").click()
        wd.find_element_by_class_name("cashboxLogout.btn.btn_transperent").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\exit_s3.png')

