from solutions.day11_SortColors import sortColors

def test_day11_01():
    test_input = [2,0,2,1,1,0]
    test_output = [0,0,1,1,2,2]
    sortColors(test_input)
    assert test_input == test_output

def test_day11_02():
    test_input = [1,1,1,1,1,1]
    test_output = [1,1,1,1,1,1]
    sortColors(test_input)
    assert test_input == test_output

def test_day11_03():
    test_input = [2,2,2,0,0,0]
    test_output = [0,0,0,2,2,2]
    sortColors(test_input)
    assert test_input == test_output
