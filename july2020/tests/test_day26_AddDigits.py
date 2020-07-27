from solutions.day26_AddDigits import addDigits

def test_day26_01():
    test_input = 38
    test_output = 2
    assert addDigits(test_input) == test_output

def test_day26_02():
    test_input = 9999
    test_output = 9
    assert addDigits(test_input) == test_output

def test_day26_03():
    test_input = 5
    test_output = 5
    assert addDigits(test_input) == test_output
