from solutions.day01_LargestTimeForGivenDigits import largestTimeFromDigits

def test_day01_01():
    test_input = [1,2,3,4]
    test_output = "23:41"
    assert largestTimeFromDigits(test_input) == test_output

def test_day01_02():
    test_input = [5,5,5,5]
    test_output = ""
    assert largestTimeFromDigits(test_input) == test_output

def test_day01_03():
    test_input = [0,0,0,0]
    test_output = "00:00"
    assert largestTimeFromDigits(test_input) == test_output

def test_day01_04():
    test_input = [0,0,1,0]
    test_output = "10:00"
    assert largestTimeFromDigits(test_input) == test_output
