from solutions.day19_SearchInRotatedSortedArray import search

def test_day19_01():
    test_nums = [4,5,6,7,0,1,2]
    test_target = 0
    test_output = 4
    assert search(test_nums, test_target) == test_output

def test_day19_02():
    test_nums = [4,5,6,7,0,1,2]
    test_target = 3
    test_output = -1
    assert search(test_nums, test_target) == test_output

def test_day19_03():
    test_nums = [1,2,3,4,5,6]
    test_target = 1
    test_output = 0
    assert search(test_nums, test_target) == test_output

def test_day19_04():
    test_nums = [5,6,1,2,3,4]
    test_target = 4
    test_output = 5
    assert search(test_nums, test_target) == test_output
