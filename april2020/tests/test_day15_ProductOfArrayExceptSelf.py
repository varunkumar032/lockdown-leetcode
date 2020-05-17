from solutions.day15_ProductOfArrayExceptSelf import productExceptSelf

def test_day15_01():
    test_input = [1,2,3,4]
    test_output = [24,12,8,6]
    assert productExceptSelf(test_input) == test_output

def test_day15_02():
    test_input = [1,2]
    test_output = [2,1]
    assert productExceptSelf(test_input) == test_output

def test_day15_03():
    test_input = [2,2,2,2]
    test_output = [8,8,8,8]
    assert productExceptSelf(test_input) == test_output

def test_day15_04():
    test_input = [1,2,0,3,4]
    test_output = [0,0,24,0,0]
    assert productExceptSelf(test_input) == test_output
