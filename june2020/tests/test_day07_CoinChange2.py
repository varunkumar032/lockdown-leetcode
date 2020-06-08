from solutions.day07_CoinChange2 import change

def test_day07_01():
    test_amount = 5
    test_coins = [1, 2, 5]
    test_output = 4
    assert change(test_amount, test_coins) == test_output

def test_day07_02():
    test_amount = 3
    test_coins = [2]
    test_output = 0
    assert change(test_amount, test_coins) == test_output

def test_day07_03():
    test_amount = 10
    test_coins = [10]
    test_output = 1
    assert change(test_amount, test_coins) == test_output
