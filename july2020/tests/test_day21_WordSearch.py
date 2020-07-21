from solutions.day21_WordSearch import exist

def test_day21_01():
    test_board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    test_word = "ABCCED"
    test_output = True
    assert exist(test_board, test_word) == test_output

def test_day21_02():
    test_board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    test_word = "SEE"
    test_output = True
    assert exist(test_board, test_word) == test_output

def test_day21_03():
    test_board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    test_word = "ABCB"
    test_output = False
    assert exist(test_board, test_word) == test_output
