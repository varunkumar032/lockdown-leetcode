from solutions.day04_RemoveCoveredIntervals import removeCoveredIntervals

def test_day04_01():
    test_input = [[1,4],[3,6],[2,8]]
    test_output = 2
    assert removeCoveredIntervals(test_input) == test_output

def test_day04_02():
    test_input = [[1,4],[2,3]]
    test_output = 1
    assert removeCoveredIntervals(test_input) == test_output

def test_day04_03():
    test_input = [[0,10],[5,12]]
    test_output = 2
    assert removeCoveredIntervals(test_input) == test_output

def test_day04_04():
    test_input = [[3,10],[4,10],[5,11]]
    test_output = 2
    assert removeCoveredIntervals(test_input) == test_output

def test_day04_05():
    test_input = [[1,2],[1,4],[3,4]]
    test_output = 1
    assert removeCoveredIntervals(test_input) == test_output
