from solutions.day25_UncrossedLines import maxUncrossedLines

def test_day25_01():
    test_A = [1,4,2]
    test_B = [1,2,4]
    test_output = 2
    assert maxUncrossedLines(test_A, test_B) == test_output

def test_day25_02():
    test_A = [2,5,1,2,5]
    test_B = [10,5,2,1,5,2]
    test_output = 3
    assert maxUncrossedLines(test_A, test_B) == test_output

def test_day25_03():
    test_A = [1,3,7,1,7,5]
    test_B = [1,9,2,5,1]
    test_output = 2
    assert maxUncrossedLines(test_A, test_B) == test_output

def test_day25_04():
    test_A = [1,1,1,1,1]
    test_B = [1,1,1,1,1]
    test_output = 5
    assert maxUncrossedLines(test_A, test_B) == test_output

def test_day25_05():
    test_A = [1,2,3,4,5]
    test_B = [6,7,8,9,10]
    test_output = 0
    assert maxUncrossedLines(test_A, test_B) == test_output
