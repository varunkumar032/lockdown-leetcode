from solutions.day13_LargestDivisibleSubset import largestDivisibleSubset

def test_day13_01():
    test_input = [1,2,3]
    test_output = [{1,2}, {1,3}]
    assert set(largestDivisibleSubset(test_input)) in test_output

def test_day13_02():
    test_input = [1,2,4,8]
    test_output = [{1,2,4,8}]
    assert set(largestDivisibleSubset(test_input)) in test_output

def test_day13_03():
    test_input = [1,4,2,6,7]
    test_output = [{1,2,4}, {1,2,6}]
    assert set(largestDivisibleSubset(test_input)) in test_output

def test_day13_04():
    test_input = [4,8,10,240]
    test_output = [{4,8,240}]
    assert set(largestDivisibleSubset(test_input)) in test_output
