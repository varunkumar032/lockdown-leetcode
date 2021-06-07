from solutions.day06_LongestConsecutiveSequence import longestConsecutive

def test_day06_01():
    test_nums = [100,4,200,1,3,2]
    test_output = 4
    assert longestConsecutive(test_nums) == test_output

def test_day06_02():
    test_nums = [0,3,7,2,5,8,4,6,0,1]
    test_output = 9
    assert longestConsecutive(test_nums) == test_output

def test_day06_03():
    test_nums = [1,2,3,4,5,6,7,8]
    test_output = 8
    assert longestConsecutive(test_nums) == test_output

def test_day06_04():
    test_nums = [8,7,6,5,4,3,2,1,0]
    test_output = 9
    assert longestConsecutive(test_nums) == test_output

def test_day06_05():
    test_nums = [8,99,7,100,6,101,5,102]
    test_output = 4
    assert longestConsecutive(test_nums) == test_output
