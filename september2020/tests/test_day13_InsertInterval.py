from solutions.day13_InsertInterval import insert

def test_day13_01():
    test_intervals = [[1,3],[6,9]]
    test_newInterval = [2, 5]
    test_output = [[1,5],[6,9]]
    assert insert(test_intervals, test_newInterval) == test_output

def test_day13_02():
    test_intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    test_newInterval = [4, 8]
    test_output = [[1,2],[3,10],[12,16]]
    assert insert(test_intervals, test_newInterval) == test_output
