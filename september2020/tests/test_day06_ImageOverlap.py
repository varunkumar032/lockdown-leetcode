from solutions.day06_ImageOverlap import largestOverlap

def test_day06_01():
    test_A = [[1,1,0], [0,1,0], [0,1,0]]
    test_B = [[0,0,0], [0,1,1], [0,0,1]]
    test_output = 3
    assert largestOverlap(test_A, test_B) == test_output
