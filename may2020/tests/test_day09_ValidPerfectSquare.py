from solutions.day09_ValidPerfectSquare import isPerfectSquare

def test_day09_01():
    test_input = 16
    test_output = True
    assert isPerfectSquare(test_input) == test_output

def test_day09_02():
    test_input = 14
    test_output = False
    assert isPerfectSquare(test_input) == test_output

def test_day09_03():
    test_input = 1
    test_output = True
    assert isPerfectSquare(test_input) == test_output
