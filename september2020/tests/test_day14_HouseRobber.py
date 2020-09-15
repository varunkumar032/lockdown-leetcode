from solutions.day14_HouseRobber import rob

def test_day14_01():
    test_nums = [1,2,3,1]
    test_output = 4
    assert rob(test_nums) == test_output

def test_day14_02():
    test_nums = [2,7,9,3,1]
    test_output = 12
    assert rob(test_nums) == test_output

def test_day14_03():
    test_nums = [5,1,1,1,1,1,5]
    test_output = 12
    assert rob(test_nums) == test_output

def test_day14_04():
    test_nums = [5,1,1,1,1,5]
    test_output = 11
    assert rob(test_nums) == test_output
