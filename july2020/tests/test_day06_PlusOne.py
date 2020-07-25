from solutions.day06_PlusOne import plusOne

def test_day06_01():
    test_input = [1,2,3]
    test_output = [1,2,4]
    assert plusOne(test_input) == test_output

def test_day06_02():
    test_input = [4,3,2,1]
    test_output = [4,3,2,2]
    assert plusOne(test_input) == test_output

def test_day06_03():
    test_input = [9,9,9,9]
    test_output = [1,0,0,0,0]
    assert plusOne(test_input) == test_output
