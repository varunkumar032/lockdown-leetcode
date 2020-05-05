from solutions.day04_MoveZeroes import moveZeroes

def test_day04_01():
    test_input = [0,1,0,3,12]
    test_output = [1,3,12,0,0]
    moveZeroes(test_input)
    assert test_input == test_output

def test_day04_02():
    test_input = [1,0,0,1]
    test_output = [1,1,0,0]
    moveZeroes(test_input)
    assert test_input == test_output

def test_day04_03():
    test_input = [1,1,1,1,1]
    test_output = [1,1,1,1,1]
    moveZeroes(test_input)
    assert test_input == test_output

def test_day04_04():
    test_input = [0,0,0,0,0]
    test_output = [0,0,0,0,0]
    moveZeroes(test_input)
    assert test_input == test_output
