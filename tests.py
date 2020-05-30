import os
import pytest
import game

# HOW TO run tests:
# coverage run -m --source=. pytest tests.py
# HOW TO get report:
# coverage report -m

empty_filename="go_test_yourself.txt"
test_filename="test_file.txt"

def setup_module():
    with open(empty_filename, "w") as file:
        pass
    with open(test_filename, "w") as file:
        file.writelines(["Corolla", "Fusion"])

def teardown_module():
    os.remove(empty_filename)
    os.remove(test_filename)

def test_word_pick_file_exists():
    assert not game.word_pick(test_filename) is None

def test_word_pick_file_does_not_exists():
    assert game.word_pick("asdf") is None

def test_word_pick_emptyfile():
    assert game.word_pick(empty_filename) is None


@pytest.mark.parametrize("word", ["GreatWall", "ToYota", "Souka"])
def test_dict_init(word):
    wgd = game.word_guessed_dict_init(word)
    assert wgd.keys() == set(word.upper()) and not any(wgd.values())


def test_dict_init_empty():
    assert game.word_guessed_dict_init("") == {}


# @pytest.mark.skipif(True, reason="skip_practice")
def test_health_lt_zero(tries_lt_0):
    assert game.health_status_str() == ""


def test_health_fails_over_total(tries_lt_fails):
    assert game.health_status_str() == "♡♡♡♡"


@pytest.mark.parametrize("char", list("TestING"))
def test_guess_ok(char, wgd):
    assert game.guess(char, wgd)


@pytest.mark.xfail()
@pytest.mark.parametrize("char", list("$\t "))
def test_guess_fails(char, wgd):
    assert game.guess(char, wgd)

def test_word_showing_endgame(wgd):
    for key in wgd: wgd[key] = True
    assert game.word_show_game("TESTING", wgd) == "T E S T I N G"

def test_word_showing_midgame(wgd):
    wgd['T'] = True
    wgd['G'] = True
    assert game.word_show_game("TESTING", wgd) == "T _ _ T _ _ G"

def test_word_showing_start(wgd):
    assert game.word_show_game("TESTING", wgd) == "_ _ _ _ _ _ _"