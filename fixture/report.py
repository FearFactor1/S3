



class ReportHelper:

    def __init__(self, app):
        self.app = app


    def calendar_today(self):
        wd = self.app.wd
        self.app.open_home_page()
        # click to report
        wd.find_element_by_link_text(u"Отчёты").click()
        # click to button report
        wd.find_element_by_class_name("btn.btn_save").click()
        # click comeback
        wd.find_element_by_link_text(u"Назад").click()
        # click close modal window
        wd.find_element_by_css_selector("div.modal__body-close").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\report\\report_today.png')