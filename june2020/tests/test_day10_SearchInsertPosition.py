from solutions.day10_SearchInsertPosition import searchInsert

def test_day10_01():
    test_nums = [1,3,5,6]
    test_target = 5
    test_output = 2
    assert searchInsert(test_nums, test_target) == test_output

def test_day10_02():
    test_nums = [1,3,5,6]
    test_target = 2
    test_output = 1
    assert searchInsert(test_nums, test_target) == test_output

def test_day10_03():
    test_nums = [1,3,5,6]
    test_target = 7
    test_output = 4
    assert searchInsert(test_nums, test_target) == test_output

def test_day10_04():
    test_nums = [1,3,5,6]
    test_target = 0
    test_output = 0
    assert searchInsert(test_nums, test_target) == test_output
