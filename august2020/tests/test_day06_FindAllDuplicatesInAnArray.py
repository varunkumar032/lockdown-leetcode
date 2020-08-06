from solutions.day06_FindAllDuplicatesInAnArray import findDuplicates

def test_day06_01():
    test_input = [4,3,2,7,8,2,3,1]
    test_output = [2,3]
    assert findDuplicates(test_input) == test_output


def test_day06_02():
    test_input = [4,2,1,3,5]
    test_output = []
    assert findDuplicates(test_input) == test_output
