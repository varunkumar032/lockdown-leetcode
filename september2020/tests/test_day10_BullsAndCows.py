from solutions.day10_BullsAndCows import getHint

def test_day10_01():
    test_secret = "1807"
    test_guess = "7810"
    test_hint = "1A3B"
    assert getHint(test_secret, test_guess) == test_hint

def test_day10_02():
    test_secret = "1123"
    test_guess = "0111"
    test_hint = "1A1B"
    assert getHint(test_secret, test_guess) == test_hint

def test_day10_03():
    test_secret = "1234"
    test_guess = "0111"
    test_hint = "0A1B"
    assert getHint(test_secret, test_guess) == test_hint

def test_day10_04():
    test_secret = "1122"
    test_guess = "1222"
    test_hint = "3A0B"
    assert getHint(test_secret, test_guess) == test_hint
