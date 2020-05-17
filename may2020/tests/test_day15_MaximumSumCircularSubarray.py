from solutions.day15_MaximumSumCircularSubarray import maxSubarraySumCircular

def test_day15_01():
    test_input = [1,-2,3,-2]
    test_output = 3
    assert maxSubarraySumCircular(test_input) == test_output

def test_day15_02():
    test_input = [5,-3,5]
    test_output = 10
    assert maxSubarraySumCircular(test_input) == test_output

def test_day15_03():
    test_input = [3,-1,2,-1]
    test_output = 4
    assert maxSubarraySumCircular(test_input) == test_output

def test_day15_04():
    test_input = [3,-2,2,-3]
    test_output = 3
    assert maxSubarraySumCircular(test_input) == test_output

def test_day15_05():
    test_input = [-2,-3,-1]
    test_output = -1
    assert maxSubarraySumCircular(test_input) == test_output
