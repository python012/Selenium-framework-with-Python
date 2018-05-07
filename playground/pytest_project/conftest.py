import pytest

@pytest.fixture(scope="session")
def get_name():
    from settings.values import NAME
    return NAME

