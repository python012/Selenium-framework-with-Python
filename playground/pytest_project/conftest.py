import pytest

@pytest.fixture(scope="session") # scope could be function(default), class, module
def get_name():
    from settings.values import NAME
    return NAME

