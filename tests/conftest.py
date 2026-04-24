import pytest
from app import repository


@pytest.fixture(autouse=True)
def clear_store():
    repository._clear_all()
    yield
    repository._clear_all()
