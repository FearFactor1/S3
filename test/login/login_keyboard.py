# Тест: Ввод логина через экранную клавиатуру



def test_screen_keyboard(app):
    app.login.press_keyboard() # ввод логина через экранную клавиатуру
    app.session.exit_s3()
