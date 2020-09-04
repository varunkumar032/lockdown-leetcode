from solutions.day03_RepeatedSubstringPattern import repeatedSubstringPattern

def test_day03_01():
    test_input = "abab"
    test_output = True
    assert repeatedSubstringPattern(test_input) == test_output

def test_day03_02():
    test_input = "aba"
    test_output = False
    assert repeatedSubstringPattern(test_input) == test_output

def test_day03_03():
    test_input = "abcabcabcabc"
    test_output = True
    assert repeatedSubstringPattern(test_input) == test_output