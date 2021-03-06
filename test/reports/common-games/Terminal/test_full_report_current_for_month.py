# Отчёт за месяц + без галочки Кассовый отчёт + Обычные + Терминал + Текущий месяц



def test_full_report_current_for_month(app):
    app.report.open_page_report()
    app.report.without_checkbox_cash_report()
    app.report.select_checkbox_for_month()
    app.report.button_get_report()
    app.report.parser_full_report_text()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_full_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_full_report_text()
    assert "  Терминал :2000006809" in app.report.parser_full_report_text()
    assert app.report.current_month_C() in app.report.parser_full_report_text()
    assert app.report.current_day_Po() in app.report.parser_full_report_text()
    app.report.comeback_main_page()