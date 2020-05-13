from solutions.day12_SingleElementInSortedArray import singleNonDuplicate

def test_day12_01():
    test_input = [1,1,4,4,5,5,6,8,8]
    test_output = 6
    assert singleNonDuplicate(test_input) == test_output

def test_day12_02():
    test_input = [1,1,4,5,5,6,6,8,8,9,9]
    test_output = 4
    assert singleNonDuplicate(test_input) == test_output

def test_day12_03():
    test_input = [1,1,4,5,5,6,6,8,8]
    test_output = 4
    assert singleNonDuplicate(test_input) == test_output

def test_day12_04():
    test_input = [1,1,4,4,5,5,6,6,8,9,9]
    test_output = 8
    assert singleNonDuplicate(test_input) == test_output

def test_day12_05():
    test_input = [1,4,4,5,5,6,6,9,9]
    test_output = 1
    assert singleNonDuplicate(test_input) == test_output

def test_day12_06():
    test_input = [1,1,4,4,5,5,6,6,9]
    test_output = 9
    assert singleNonDuplicate(test_input) == test_output

def test_day12_07():
    test_input = [1]
    test_output = 1
    assert singleNonDuplicate(test_input) == test_output
