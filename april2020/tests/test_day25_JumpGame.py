from solutions.day25_JumpGame import canJump

def test_day25_01():
    test_input = [2,3,1,1,4]
    test_output = True
    assert canJump(test_input) == test_output

def test_day25_02():
    test_input = [3,2,1,0,4]
    test_output = False
    assert canJump(test_input) == test_output

def test_day25_03():
    test_input = [5,5,5,5,5]
    test_output = True
    assert canJump(test_input) == test_output

def test_day25_04():
    test_input = [0,1,2,3,4,5]
    test_output = False
    assert canJump(test_input) == test_output
