from solutions.day19_MinimumDominoRotationsForEqualRow import minDominoRotations

def test_day19_01():
    test_A = [2,1,2,4,2,2]
    test_B = [5,2,6,2,3,2]
    test_output = 2
    assert minDominoRotations(test_A, test_B) == test_output

def test_day19_02():
    test_A = [3,5,1,2,3]
    test_B = [3,6,3,3,4]
    test_output = -1
    assert minDominoRotations(test_A, test_B) == test_output

def test_day19_03():
    test_A = [1,2,1,1,1,2,2]
    test_B = [2,1,2,2,2,1,2]
    test_output = 2
    assert minDominoRotations(test_A, test_B) == test_output
