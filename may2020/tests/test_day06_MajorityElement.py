from solutions.day06_MajorityElement import majorityElement

def test_day06_01():
    test_input = [3,2,3]
    test_output = 3
    assert majorityElement(test_input) == test_output

def test_day06_02():
    test_input = [2,2,1,1,1,2,2]
    test_output = 2
    assert majorityElement(test_input) == test_output
