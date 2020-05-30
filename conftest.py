import pytest
import game


@pytest.fixture
def tries_lt_fails():
    game.user_fails = 5
    game.user_tries = 4

@pytest.fixture()
def tries_lt_0():
    game.user_tries = -2

@pytest.fixture
def wgd():
    return {
        'T': False,
        'E': False,
        'S': False,
        'I': False,
        'N': False,
        'G': False
        }