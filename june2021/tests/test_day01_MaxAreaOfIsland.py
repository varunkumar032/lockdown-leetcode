from solutions.day01_MaxAreaOfIsland import maxAreaOfIsland

def test_day01_01():
    test_grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
    			 [0,1,1,0,1,0,0,0,0,0,0,0,0],
    			 [0,1,0,0,1,1,0,0,1,0,1,0,0],
    			 [0,1,0,0,1,1,0,0,1,1,1,0,0],
    			 [0,0,0,0,0,0,0,0,0,0,1,0,0],
    			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
    			 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    test_output = 6
    assert maxAreaOfIsland(test_grid) == test_output

def test_day01_02():
    test_grid = [[0,0,0,0,0,0,0,0]]
    test_output = 0
    assert maxAreaOfIsland(test_grid) == test_output


def test_day01_03():
    test_grid = [[1,1,1,1],
    			 [1,1,1,1],
    			 [1,1,1,1],
    			 [1,1,1,1]]
    test_output = 16
    assert maxAreaOfIsland(test_grid) == test_output

def test_day01_04():
    test_grid = [[1,0.0,1],
    			 [0,0,0,0],
    			 [0,0,0,0],
    			 [1,0,0,1]]
    test_output = 1
    assert maxAreaOfIsland(test_grid) == test_output
