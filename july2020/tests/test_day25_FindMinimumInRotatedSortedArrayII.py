from solutions.day25_FindMinimumInRotatedSortedArrayII import findMin

def test_day25_01():
    test_nums = [1,3,5]
    test_output = 1
    assert findMin(test_nums) == test_output

def test_day25_02():
    test_nums = [2,2,2,0,1]
    test_output = 0
    assert findMin(test_nums) == test_output

def test_day25_03():
    test_nums = [6,7,1,2,3,4,5]
    test_output = 1
    assert findMin(test_nums) == test_output

def test_day25_04():
    test_nums = [4,5,6,7,1,2,3]
    test_output = 1
    assert findMin(test_nums) == test_output

def test_day25_05():
    test_nums = [1,2]
    test_output = 1
    assert findMin(test_nums) == test_output

def test_day25_06():
    test_nums = [2,1]
    test_output = 1
    assert findMin(test_nums) == test_output
