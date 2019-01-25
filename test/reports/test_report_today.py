import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_report_today(app):
    app.login(username="20003510", password="34756381")
    app.report_today()
    app.exit_s3()
