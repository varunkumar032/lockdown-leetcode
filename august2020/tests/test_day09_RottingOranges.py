from solutions.day09_RottingOranges import orangesRotting

def test_day09_01():
    test_input = [[2,1,1],[1,1,0],[0,1,1]]
    test_output = 4
    assert orangesRotting(test_input) == test_output

def test_day09_02():
    test_input = [[2,1,1],[0,1,1],[1,0,1]]
    test_output = -1
    assert orangesRotting(test_input) == test_output

def test_day09_03():
    test_input = [[0,2]]
    test_output = 0
    assert orangesRotting(test_input) == test_output

def test_day09_04():
    test_input = [[2,1,1,1],[1,1,1,1],[1,1,1,1]]
    test_output = 5
    assert orangesRotting(test_input) == test_output
