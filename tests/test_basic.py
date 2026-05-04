from from_roman_to_english import roman_to_int
from max_number import find_max
from number_to_words import number_to_words
from roll_dice import Dice
from sigma import build_sigma
from symbol_to_emoji import emojify_text


def test_roman_basic():
    assert roman_to_int("XII") == 12
    assert roman_to_int("IX") == 9


def test_find_max():
    assert find_max([1, 3, 2]) == 3


def test_number_to_words():
    assert number_to_words("201") == "two zero one"


def test_dice_roll():
    r = Dice().roll()
    assert isinstance(r, tuple) and len(r) == 2
    assert all(1 <= x <= 6 for x in r)


def test_sigma():
    assert build_sigma() == "sigma"


def test_emojify_text():
    assert emojify_text(":) :(") == "🙂 🙁"
