from solutions.day08_PowerOfTwo import isPowerOfTwo

def test_day08_01():
    test_input = 1
    test_output = True
    assert isPowerOfTwo(test_input) == test_output

def test_day08_02():
    test_input = 16
    test_output = True
    assert isPowerOfTwo(test_input) == test_output

def test_day08_03():
    test_input = 218
    test_output = False
    assert isPowerOfTwo(test_input) == test_output

def test_day08_04():
    test_input = 0
    test_output = False
    assert isPowerOfTwo(test_input) == test_output
