from solutions.day07_IslandPerimeter import islandPerimeter

def test_day07_01():
    test_input = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    test_output = 16
    assert islandPerimeter(test_input) == test_output

def test_day07_02():
    test_input = [[0,0,0,0], [0,1,1,0], [0,1,1,0], [0,0,0,0]]
    test_output = 8
    assert islandPerimeter(test_input) == test_output

def test_day07_03():
    test_input = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    test_output = 16
    assert islandPerimeter(test_input) == test_output

def test_day07_04():
    test_input = [[0,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,0,0]]
    test_output = 4
    assert islandPerimeter(test_input) == test_output
