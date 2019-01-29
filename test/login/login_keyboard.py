# Тест: Ввод логина через экранную клавиатуру
import pytest
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_screen_keyboard(app):
    app.login.login_keyboard() # ввод логина через экранную клавиатуру
    app.session.exit_s3()
