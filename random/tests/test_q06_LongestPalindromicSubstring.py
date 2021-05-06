from solutions.q06_LongestPalindromicSubstring import longestPalindrome

def test_q06_01():
    test_s = "babad"
    test_output = ["bab", "aba"]
    assert longestPalindrome(test_s) in test_output

def test_q06_02():
    test_s = "cbbd"
    test_output = ["bb"]
    assert longestPalindrome(test_s) in test_output

def test_q06_03():
    test_s = "a"
    test_output = ["a"]
    assert longestPalindrome(test_s) in test_output

def test_q06_04():
    test_s = "ac"
    test_output = ["a", "c"]
    assert longestPalindrome(test_s) in test_output
