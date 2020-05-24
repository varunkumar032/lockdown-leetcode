from solutions.day21_CountSquareSubmatricesWithAllOnes import countSquares

def test_day21_01():
    test_input_matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    test_output = 15
    assert countSquares(test_input_matrix) == test_output

def test_day21_02():
    test_input_matrix = [[1,0,1],[1,1,0],[1,1,0]]
    test_output = 7
    assert countSquares(test_input_matrix) == test_output

def test_day21_03():
    test_input_matrix = [[1,1,1],[1,1,1],[1,1,1]]
    test_output = 14
    assert countSquares(test_input_matrix) == test_output

def test_day21_04():
    test_input_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    test_output = 0
    assert countSquares(test_input_matrix) == test_output
