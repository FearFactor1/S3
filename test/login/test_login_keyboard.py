# Тест: Ввод логина через экранную клавиатуру



def test_screen_keyboard(app):
    app.login.press_keyboard() # ввод логина через экранную клавиатуру
    app.login.user_in_main_page()
    app.session.exit_s3()