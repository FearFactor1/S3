from datetime import datetime



class ReportHelper:

    def __init__(self, app):
        self.app = app

# ----- основные методы фикстуры reports

    def parser_report_text(self):
        wd = self.app.wd
        if len(wd.find_element_by_css_selector("pre").text) > 0:
            test = wd.find_element_by_css_selector("pre").text
            spl = test.split('\n')
        else:
            print("Пустой тег в отчёте")
        #print(' | '.join(spl))
        return test


    def parser_full_report_text(self):
        wd = self.app.wd
        if len(wd.find_element_by_css_selector("pre").text) > 0:
            textfull = wd.find_element_by_css_selector("pre").text
        assert textfull.count('Кено Спортлото') == 3
        assert textfull.count('ГОСЛОТО 4 из 20') == 3
        assert textfull.count('ГОСЛОТО 6 из 45') == 3
        assert textfull.count('ГОСЛОТО 7 из 49') == 3
        assert textfull.count('5х36 до тиража 7268') == 3
        assert textfull.count('Рапидо') == 6
        assert textfull.count('Рапидо2') == 3
        assert textfull.count('Спортлото 6 из 49') == 3
        assert textfull.count('Гослото 5 из 36') == 3
        assert textfull.count('Спортлото Матчбол') == 3
        assert textfull.count('6 из 36') == 3
        assert textfull.count('Русское Лото') == 3
        assert textfull.count('Жилищная лотерея') == 3
        assert textfull.count('Золотая подкова') == 3
        assert textfull.count('Бинго 80') == 3
        assert textfull.count('Бинго 75') == 3
        assert textfull.count('12x24') == 3
        assert textfull.count('Прикуп') == 3
        assert textfull.count('Дуэль') == 3
        assert textfull.count('Зодиак') == 3
        assert textfull.count('Джокер') == 3
        assert textfull.count('Моментальные') == 3
        assert 'Продажи' in textfull
        assert 'Отмены' in textfull
        assert 'Выплаты' in textfull
        assert textfull.count('ИТОГО') == 4
        assert 'ИТОГО ПО ОТЧЕТУ' in textfull
        return textfull
        #print(re.findall('Рапидо', textfull))


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


    def current_day_C(self):
        d = datetime.today().strftime('%d/%m/%Y 00:00:00')
        c = " C  " + ":  " + d
        #print(c)
        return c


    def current_month_C(self):
        dm = datetime.today().strftime('%m/%Y 00:00:00')
        cm = " C  " + ":  " + "01/" + dm
        #print(cm)
        return cm


    def current_day_Po(self):
        dp = datetime.today().strftime('%d/%m/%Y %H:%M')
        Po = " По " + ":  " + dp
        #print(Po)
        return Po


    def without_checkbox_cash_report(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType1']").click()


    def select_checkbox_for_month(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType3']").click()


    def select_user(self):
        wd = self.app.wd
        wd.find_element_by_name("reportUserType").click()
        wd.find_element_by_css_selector("option[value='USER']").click()


    def previous_month_date_10(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.ui-datepicker-prev.ui-corner-all").click()
        wd.find_element_by_xpath("//a[contains(text(),'10')]").click()


    def previous_month_date_1(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.ui-datepicker-prev.ui-corner-all").click()
        wd.find_element_by_xpath("//a[contains(text(),'1')]").click()