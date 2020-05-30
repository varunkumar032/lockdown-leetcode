from solutions.day27_PossibleBipartition import possibleBipartition

def test_day27_01():
    test_N = 4
    test_dislikes = [[1,2],[1,3],[2,4]]
    test_output = True
    assert possibleBipartition(test_N, test_dislikes) == test_output

def test_day27_02():
    test_N = 3
    test_dislikes = [[1,2],[1,3],[2,3]]
    test_output = False
    assert possibleBipartition(test_N, test_dislikes) == test_output

def test_day27_03():
    test_N = 5
    test_dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    test_output = False
    assert possibleBipartition(test_N, test_dislikes) == test_output

def test_day27_04():
    test_N = 1
    test_dislikes = []
    test_output = True
    assert possibleBipartition(test_N, test_dislikes) == test_output

def test_day27_05():
    test_N = 10
    test_dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
    test_output = True
    assert possibleBipartition(test_N, test_dislikes) == test_output
