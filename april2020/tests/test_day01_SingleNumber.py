from solutions.day01_SingleNumber import singleNumber

def test_day01_01():
    test_input = [2,2,1]
    test_output = 1
    assert singleNumber(test_input) == test_output

def test_day01_02():
    test_input = [4,1,2,1,2]
    test_output = 4
    assert singleNumber(test_input) == test_output

def test_day01_03():
    test_input = [1,2,1,2]
    test_output = 0
    assert singleNumber(test_input) == test_output

def test_day01_04():
    test_input = [1]
    test_output = 1
    assert singleNumber(test_input) == test_output
