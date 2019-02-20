# Тест: 0051 Неверный идентификатор пользователя терминала




def test_error_login(app):
    app.login.incorrect_user()