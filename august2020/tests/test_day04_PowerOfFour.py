from solutions.day04_PowerOfFour import isPowerOfFour

def test_day04_01():
    test_input = 16
    test_output = True
    assert isPowerOfFour(test_input) == test_output

def test_day04_02():
    test_input = 5
    test_output = False
    assert isPowerOfFour(test_input) == test_output

def test_day04_03():
    test_input = 1
    test_output = True
    assert isPowerOfFour(test_input) == test_output

def test_day04_04():
    test_input = 0
    test_output = False
    assert isPowerOfFour(test_input) == test_output
