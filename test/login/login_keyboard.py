# Тест: Ввод логина через экранную клавиатуру



def test_screen_keyboard(app):
    app.login.login_keyboard() # ввод логина через экранную клавиатуру
    app.session.exit_s3()
