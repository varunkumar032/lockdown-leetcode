from solutions.day26_ContiguousArray import findMaxLength

def test_day26_01():
    test_input = [0,1]
    test_output = 2
    assert findMaxLength(test_input) == test_output

def test_day26_02():
    test_input = [0,1,0]
    test_output = 2
    assert findMaxLength(test_input) == test_output

def test_day26_03():
    test_input = [0,0,1,0,0,1,1]
    test_output = 6
    assert findMaxLength(test_input) == test_output

def test_day26_04():
    test_input = [0]
    test_output = 0
    assert findMaxLength(test_input) == test_output
