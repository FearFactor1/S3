# Тест: Ввод логина и разлогин



def test_login(app2):
    app2.login.correct_user()
    app2.login.user_in_main_page()
    app2.session.exit_s3()