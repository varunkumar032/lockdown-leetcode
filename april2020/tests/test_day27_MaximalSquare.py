from solutions.day27_MaximalSquare import maximalSquare

def test_day27_01():
    test_matrix = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]
    test_output = 4
    assert maximalSquare(test_matrix) == test_output

def test_day27_02():
    test_matrix = [['0','0','0'],['0','0','0'],['0','0','0']]
    test_output = 0
    assert maximalSquare(test_matrix) == test_output

def test_day27_03():
    test_matrix = [['0','1','0'],['0','0','0'],['0','0','0']]
    test_output = 1
    assert maximalSquare(test_matrix) == test_output

def test_day27_04():
    test_matrix = [['1','1','1'],['1','1','1'],['1','1','1']]
    test_output = 9
    assert maximalSquare(test_matrix) == test_output
