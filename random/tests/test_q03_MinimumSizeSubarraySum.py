from solutions.q03_MinimumSizeSubarraySum import minSubArrayLen

def test_q03_01():
    test_s = 7
    test_nums = [2,3,1,2,4,3]
    test_output = 2
    assert minSubArrayLen(test_s, test_nums) == test_output

def test_q03_02():
    test_s = 77
    test_nums = [2,3,1,2,4,3]
    test_output = 0
    assert minSubArrayLen(test_s, test_nums) == test_output

def test_q03_03():
    test_s = 15
    test_nums = [1,2,3,4,5]
    test_output = 5
    assert minSubArrayLen(test_s, test_nums) == test_output

def test_q03_04():
    test_s = 5
    test_nums = [2,1,2,3,5]
    test_output = 1
    assert minSubArrayLen(test_s, test_nums) == test_output

def test_q03_05():
    test_s = 5
    test_nums = [1,0,0,2,3]
    test_output = 2
    assert minSubArrayLen(test_s, test_nums) == test_output
