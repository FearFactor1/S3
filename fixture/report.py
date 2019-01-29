



class ReportHelper:

    def __init__(self, app):
        self.app = app


    def report_today(self):
        wd = self.app.wd
        self.app.open_home_page()
        # click to report
        wd.find_element_by_link_text(u"Отчёты").click()
        # click to button report
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кассовый отчет'])[1]/following::button[1]").click()
        # click comeback
        wd.find_element_by_link_text(u"Назад").click()
        # click close modal window
        wd.find_element_by_css_selector("div.modal__body-close").click()