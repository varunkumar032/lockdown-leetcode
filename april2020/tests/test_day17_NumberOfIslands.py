from solutions.day17_NumberOfIslands import numIslands

def test_day17_01():
    test_grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
    test_output = 1
    assert numIslands(test_grid) == test_output

def test_day17_02():
    test_grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    test_output = 3
    assert numIslands(test_grid) == test_output

def test_day17_03():
    test_grid = [['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1']]
    test_output = 1
    assert numIslands(test_grid) == test_output
