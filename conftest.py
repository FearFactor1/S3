import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="20003510", password="34756381")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="20003510", password="34756381")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.exit_s3()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture