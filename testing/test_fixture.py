import pytest

@pytest.fixture
def setup_list()->list:
    return ['apple','banana']

def test_apple(setup_list):
    assert 'apple' in setup_list

def test_mango(setup_list):
    assert 'mango' in setup_list

def test_banana(setup_list):
    assert 'banana' in setup_list
