from datetime import datetime, date, time



class ReportHelper:

    def __init__(self, app):
        self.app = app

# ----- основные методы фикстуры reports

    def parser_report_text(self):
        wd = self.app.wd
        #test = wd.find_element_by_css_selector("center > strong").text
        #test = test.replace('\n', ' ')
        #assert test == "ОТЧЕТ ЗА ДЕНЬ ИТОГИ ПО ТЕРМИНАЛУ"
        if len(wd.find_element_by_css_selector("center").text) > 0:
            test = wd.find_element_by_css_selector("center").text
            c = datetime.today().strftime('%d/%m/%Y 00:00:00')
            spl = test.split('\n')
        else:
            print("Пустой тег в отчёте")
        assert " C  " + ":  " + c in spl
        print(' | '.join(spl))
        print(c)
        return spl


    def comeback_main_page(self):
        wd = self.app.wd
        # click comeback
        wd.find_element_by_link_text(u"Назад").click()
        # click close modal window
        wd.find_element_by_css_selector("div.modal__body-close").click()


    def button_get_report(self):
        wd = self.app.wd
        wd.find_element_by_class_name("btn.btn_save").click()


    def open_page_report(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Отчёты").click()
