# Тест: Ввод логина и разлогин



def test_login(app):
    app.login.correct_user()
    app.login.user_in_main_page()
    app.session.exit_s3()