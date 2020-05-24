from solutions.day21_LeftmostColumnWithAtleastAOne import leftMostColumnWithOne

def test_day21_01():
    test_input_mat = [[0,0],[1,1]]
    test_output = 0
    assert leftMostColumnWithOne(test_input_mat) == test_output

def test_day21_02():
    test_input_mat = [[0,0],[0,1]]
    test_output = 1
    assert leftMostColumnWithOne(test_input_mat) == test_output

def test_day21_03():
    test_input_mat = [[0,0],[0,0]]
    test_output = -1
    assert leftMostColumnWithOne(test_input_mat) == test_output

def test_day21_04():
    test_input_mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    test_output = 1
    assert leftMostColumnWithOne(test_input_mat) == test_output
