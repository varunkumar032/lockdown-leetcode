from solutions.day29_UniquePaths import uniquePaths

def test_day29_01():
    test_m = 3
    test_n = 2
    test_output = 3
    assert uniquePaths(test_m, test_n) == test_output

def test_day29_02():
    test_m = 7
    test_n = 3
    test_output = 28
    assert uniquePaths(test_m, test_n) == test_output

def test_day29_03():
    test_m = 1
    test_n = 3
    test_output = 1
    assert uniquePaths(test_m, test_n) == test_output

def test_day29_04():
    test_m = 3
    test_n = 1
    test_output = 1
    assert uniquePaths(test_m, test_n) == test_output
