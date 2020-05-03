from solutions.day02_HappyNumber import isHappy

def test_day02_01():
    test_input = 19
    test_output = True
    assert isHappy(test_input) == test_output

def test_day02_02():
    test_input = 20
    test_output = False
    assert isHappy(test_input) == test_output

def test_day02_03():
    test_input = 1
    test_output = True
    assert isHappy(test_input) == test_output

