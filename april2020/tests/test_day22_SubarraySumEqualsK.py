from solutions.day22_SubarraySumEqualsK import subarraySum

def test_day22_01():
    test_input_nums = [1,1,1]
    test_input_k = 2
    test_output = 2
    assert subarraySum(test_input_nums, test_input_k) == test_output

def test_day22_02():
    test_input_nums = [1,2,1,3,2,-3,1,3]
    test_input_k = 3
    test_output = 7
    assert subarraySum(test_input_nums, test_input_k) == test_output

def test_day22_03():
    test_input_nums = [1]
    test_input_k = 0
    test_output = 0
    assert subarraySum(test_input_nums, test_input_k) == test_output
