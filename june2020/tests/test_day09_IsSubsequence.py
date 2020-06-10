from solutions.day09_IsSubsequence import isSubsequence

def test_day09_01():
    test_s = "abc"
    test_t = "ahbgdc"
    test_output = True
    assert isSubsequence(test_s, test_t) == test_output

def test_day09_02():
    test_s = "axc"
    test_t = "ahbgdc"
    test_output = False
    assert isSubsequence(test_s, test_t) == test_output

def test_day09_03():
    test_s = "acb"
    test_t = "ahbgdc"
    test_output = False
    assert isSubsequence(test_s, test_t) == test_output
