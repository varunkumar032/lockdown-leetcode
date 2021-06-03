from solutions.day02_InterleavingString import isInterleave

def test_day02_01():
    test_s1 = "aabcc"
    test_s2 = "dbbca"
    test_s3 = "aadbbcbcac"
    test_output = True
    assert isInterleave(test_s1, test_s2, test_s3) == test_output

def test_day02_02():
    test_s1 = "aabcc"
    test_s2 = "dbbca"
    test_s3 = "aadbbbaccc"
    test_output = False
    assert isInterleave(test_s1, test_s2, test_s3) == test_output

def test_day02_03():
    test_s1 = ""
    test_s2 = ""
    test_s3 = ""
    test_output = True
    assert isInterleave(test_s1, test_s2, test_s3) == test_output
