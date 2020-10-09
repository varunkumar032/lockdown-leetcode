from solutions.q01_twoSum import twoSum

def test_01():
    test_nums = [2,7,11,15]
    test_target = 9
    test_output = [0,1]
    assert twoSum(test_nums, test_target) == test_output

def test_02():
    test_nums = [3,2,4]
    test_target = 6
    test_output = [1,2]
    assert twoSum(test_nums, test_target) == test_output

def test_03():
    test_nums = [3,3]
    test_target = 6
    test_output = [0,1]
    assert twoSum(test_nums, test_target) == test_output

def test_04():
    test_nums = [2,7,11,15]
    test_target = 10
    test_output = [-1,-1]
    assert twoSum(test_nums, test_target) == test_output
