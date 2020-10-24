from solutions.day23_132Pattern import find132pattern

def test_day23_01():
    test_input = [1,2,3,4]
    test_output = False
    assert find132pattern(test_input) == test_output

def test_day23_02():
    test_input = [3,1,4,2]
    test_output = True
    assert find132pattern(test_input) == test_output

def test_day23_03():
    test_input = [-1,3,2,0]
    test_output = True
    assert find132pattern(test_input) == test_output

def test_day23_04():
    test_input = [6,12,3,4,6,11,20]
    test_output = True
    assert find132pattern(test_input) == test_output

def test_day23_05():
    test_input = [3,1,4,0]
    test_output = False
    assert find132pattern(test_input) == test_output