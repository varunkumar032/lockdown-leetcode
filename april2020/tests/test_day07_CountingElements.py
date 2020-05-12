from solutions.day07_CountingElements import countElements

def test_day07_01():
    test_input = [1,2,3]
    test_output = 2
    assert countElements(test_input) == test_output

def test_day07_02():
    test_input = [1,1,3,3,5,5,7,7]
    test_output = 0
    assert countElements(test_input) == test_output

def test_day07_03():
    test_input = [1,3,2,3,5,0]
    test_output = 3
    assert countElements(test_input) == test_output

def test_day07_04():
    test_input = [1,1,2,2]
    test_output = 2
    assert countElements(test_input) == test_output
