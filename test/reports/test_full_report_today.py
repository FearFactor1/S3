# Отчёт за день + без галочки Кассовый отчёт + Обычные + Терминал + Текущая дата



def test_full_report_today(app):
    app.report.open_page_report()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_report_text()
    app.report.comeback_main_page()
