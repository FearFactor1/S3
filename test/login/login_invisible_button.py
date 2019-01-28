# Тест: Кнопка Войти не доступна после кликов на поле логин и пароль
import pytest
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_invisible_button(app):
    app.login_invisible_button() # проверка, что кнопка Войти не доступна





