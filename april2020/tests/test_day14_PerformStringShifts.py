from solutions.day14_PerformStringShifts import stringShift

def test_day14_01():
    test_s = "abc"
    test_shift = [[0,1],[1,2]]
    test_output = "cab"
    assert stringShift(test_s, test_shift) == test_output

def test_day14_02():
    test_s = "abcdefg"
    test_shift = [[1,1],[1,1],[0,2],[1,3]]
    test_output = "efgabcd"
    assert stringShift(test_s, test_shift) == test_output

def test_day14_03():
    test_s = "a"
    test_shift = [[0,1],[1,2]]
    test_output = "a"
    assert stringShift(test_s, test_shift) == test_output

def test_day14_04():
    test_s = "abcdefg"
    test_shift = [[0,10],[1,20]]
    test_output = "efgabcd"
    assert stringShift(test_s, test_shift) == test_output
