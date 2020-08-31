from solutions.day29_PancakeSorting import pancakeSort

def test_day29_01():
    test_input = [3,2,4,1]
    test_output = [3,4,2,3,2]
    assert pancakeSort(test_input) == test_output

def test_day29_02():
    test_input = [1,2,3]
    test_output = []
    assert pancakeSort(test_input) == test_output
