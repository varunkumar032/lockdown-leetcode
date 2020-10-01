from solutions.day29_WordBreak import wordBreak

def test_day29_01():
    test_s = "leetcode"
    test_worddict = ["leet", "code"]
    test_output = True
    assert wordBreak(test_s, test_worddict) == test_output

def test_day29_02():
    test_s = "applepenapple"
    test_worddict = ["apple", "pen"]
    test_output = True
    assert wordBreak(test_s, test_worddict) == test_output

def test_day29_03():
    test_s = "catsandog"
    test_worddict = ["cats", "dog", "sand", "and", "cat"]
    test_output = False
    assert wordBreak(test_s, test_worddict) == test_output
