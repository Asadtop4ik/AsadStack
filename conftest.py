import pytest
from Asad_Stack.app import AsadStackApp


@pytest.fixture
def app():
    return AsadStackApp()


@pytest.fixture
def test_client(app):
    return app.test_session()
