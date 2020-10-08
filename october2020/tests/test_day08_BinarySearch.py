from solutions.day08_BinarySearch import search

def test_day08_01():
    test_nums = [-1,0,3,5,9,12]
    test_target = 9
    test_output = 4
    assert search(test_nums, test_target) == test_output

def test_day08_02():
    test_nums = [-1,0,3,5,9,12]
    test_target = 2
    test_output = -1
    assert search(test_nums, test_target) == test_output
