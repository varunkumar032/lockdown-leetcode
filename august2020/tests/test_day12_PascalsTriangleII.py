from solutions.day12_PascalsTriangleII import getRow

def test_day12_01():
    test_input = 3
    test_output = [1, 3, 3, 1]
    assert getRow(test_input) == test_output

def test_day12_02():
    test_input = 1
    test_output = [1, 1]
    assert getRow(test_input) == test_output

def test_day12_03():
    test_input = 0
    test_output = [1]
    assert getRow(test_input) == test_output
