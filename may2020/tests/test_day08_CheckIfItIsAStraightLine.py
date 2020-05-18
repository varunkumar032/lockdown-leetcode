from solutions.day08_CheckIfItIsAStraightLine import checkStraightLine

def test_day08_01():
    test_coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    test_output = True
    assert checkStraightLine(test_coordinates) == test_output

def test_day08_02():
    test_coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    test_output = False
    assert checkStraightLine(test_coordinates) == test_output

def test_day08_03():
    test_coordinates = [[1,1],[2,2]]
    test_output = True
    assert checkStraightLine(test_coordinates) == test_output
