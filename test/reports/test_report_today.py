


def test_report_today(app):
    app.session.login(username="20003510", password="34756381")
    app.report.report_today()
    app.session.exit_s3()
