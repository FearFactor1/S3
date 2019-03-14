# Тест: 0051 Неверный идентификатор пользователя терминала




def test_error_login(app2):
    app2.login.incorrect_user()