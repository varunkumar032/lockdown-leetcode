from solutions.day12_LastStoneWeight import lastStoneWeight

def test_day12_01():
    test_input = [2,7,4,1,8,1]
    test_output = 1
    assert lastStoneWeight(test_input) == test_output

def test_day12_02():
    test_input = [5]
    test_output = 5
    assert lastStoneWeight(test_input) == test_output

def test_day12_03():
    test_input = [5,5,5,5,5]
    test_output = 5
    assert lastStoneWeight(test_input) == test_output

def test_day12_04():
    test_input = [5,5,5,5]
    test_output = 0
    assert lastStoneWeight(test_input) == test_output
