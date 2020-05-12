from solutions.day11_FloodFill import floodFill

def test_day11_01():
    test_image = [[1,1,1],[1,1,0],[1,0,1]]
    test_sr = 1
    test_sc = 1
    test_newColor = 2
    test_output = [[2,2,2],[2,2,0],[2,0,1]]
    assert floodFill(test_image, test_sr, test_sc, test_newColor) == test_output

def test_day11_02():
    test_image = [[1,1,1],[1,2,0],[1,0,1]]
    test_sr = 1
    test_sc = 1
    test_newColor = 2
    test_output = [[1,1,1],[1,2,0],[1,0,1]]
    assert floodFill(test_image, test_sr, test_sc, test_newColor) == test_output

def test_day11_03():
    test_image = [[1,1,1],[1,1,1],[1,1,1]]
    test_sr = 1
    test_sc = 1
    test_newColor = 2
    test_output = [[2,2,2],[2,2,2],[2,2,2]]
    assert floodFill(test_image, test_sr, test_sc, test_newColor) == test_output
