from solutions.day26_LongestCommonSubsequence import longestCommonSubsequence

def test_day26_01():
    test_text1 = "abcde"
    test_text2 = "ace"
    test_output = 3
    assert longestCommonSubsequence(test_text1, test_text2) == test_output

def test_day26_02():
    test_text1 = "abc"
    test_text2 = "abc"
    test_output = 3
    assert longestCommonSubsequence(test_text1, test_text2) == test_output

def test_day26_03():
    test_text1 = "abc"
    test_text2 = "def"
    test_output = 0
    assert longestCommonSubsequence(test_text1, test_text2) == test_output

def test_day26_04():
    test_text1 = "abc"
    test_text2 = ""
    test_output = 0
    assert longestCommonSubsequence(test_text1, test_text2) == test_output
