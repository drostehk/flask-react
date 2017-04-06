from app.factory import create_app
import pytest


@pytest.fixture
def app():
    application = create_app(config='Testing',
                             instance=False)
    return application
