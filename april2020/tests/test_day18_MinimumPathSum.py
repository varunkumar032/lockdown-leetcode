from solutions.day18_MinimumPathSum import minPathSum

def test_day18_01():
    test_grid = [[1,3,1],[1,5,1],[4,2,1]]
    test_output = 7
    assert minPathSum(test_grid) == test_output

def test_day18_02():
    test_grid = [[1,1,1],[1,1,1],[1,1,1]]
    test_output = 5
    assert minPathSum(test_grid) == test_output

def test_day18_03():
    test_grid = [[1,2],[3,4]]
    test_output = 7
    assert minPathSum(test_grid) == test_output

def test_day18_04():
    test_grid = [[1]]
    test_output = 1
    assert minPathSum(test_grid) == test_output
