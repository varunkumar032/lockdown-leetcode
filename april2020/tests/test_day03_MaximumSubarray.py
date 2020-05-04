from solutions.day03_MaximumSubarray import maxSubArray

def test_day03_01():
    test_input = [-2,1,-3,4,-1,2,1,-5,4]
    test_output = 6
    assert maxSubArray(test_input) == test_output

def test_day03_02():
    test_input = [5]
    test_output = 5
    assert maxSubArray(test_input) == test_output

def test_day03_03():
    test_input = [1,1,1,1]
    test_output = 4
    assert maxSubArray(test_input) == test_output

def test_day03_04():
    test_input = [-1,-1,-1,-1]
    test_output = -1
    assert maxSubArray(test_input) == test_output
