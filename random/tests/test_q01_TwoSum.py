from solutions.q01_TwoSum import twoSum

def test_q01_01():
    test_nums = [2,7,11,15]
    test_target = 9
    test_output = [0,1]
    assert twoSum(test_nums, test_target) == test_output

def test_q01_02():
    test_nums = [3,2,4]
    test_target = 6
    test_output = [1,2]
    assert twoSum(test_nums, test_target) == test_output

def test_q01_03():
    test_nums = [3,3]
    test_target = 6
    test_output = [0,1]
    assert twoSum(test_nums, test_target) == test_output

def test_q01_04():
    test_nums = [2,7,11,15]
    test_target = 10
    test_output = [-1,-1]
    assert twoSum(test_nums, test_target) == test_output
