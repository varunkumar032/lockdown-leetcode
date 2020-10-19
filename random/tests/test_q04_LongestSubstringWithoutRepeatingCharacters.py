from solutions.q04_LongestSubstringWithoutRepeatingCharacters import lengthOfLongestSubstring

def test_q04_01():
    test_s = "abcabcbb"
    test_output = 3
    assert lengthOfLongestSubstring(test_s) == test_output

def test_q04_02():
    test_s = "bbbbb"
    test_output = 1
    assert lengthOfLongestSubstring(test_s) == test_output

def test_q04_03():
    test_s = "pwwkew"
    test_output = 3
    assert lengthOfLongestSubstring(test_s) == test_output

def test_q04_04():
    test_s = ""
    test_output = 0
    assert lengthOfLongestSubstring(test_s) == test_output

def test_q04_05():
    test_s = "au"
    test_output = 2
    assert lengthOfLongestSubstring(test_s) == test_output
