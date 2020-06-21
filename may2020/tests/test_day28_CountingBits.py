from solutions.day28_CountingBits import countBits

def test_day28_01():
    test_input = 2
    test_output = [0,1,1]
    assert countBits(test_input) == test_output

def test_day28_02():
    test_input = 5
    test_output = [0,1,1,2,1,2]
    assert countBits(test_input) == test_output

def test_day28_03():
    test_input = 0
    test_output = [0]
    assert countBits(test_input) == test_output
