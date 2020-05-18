from solutions.day17_FindAllAnagramsInAString import findAnagrams

def test_day17_01():
    test_s = "cbaebabacd"
    test_p = "abc"
    test_output = [0, 6]
    assert findAnagrams(test_s, test_p) == test_output

def test_day17_02():
    test_s = "abab"
    test_p = "ab"
    test_output = [0, 1, 2]
    assert findAnagrams(test_s, test_p) == test_output

def test_day17_03():
    test_s = "aaaaaa"
    test_p = "aaa"
    test_output = [0, 1, 2, 3]
    assert findAnagrams(test_s, test_p) == test_output

def test_day17_04():
    test_s = "abcab"
    test_p = "abcdef"
    test_output = []
    assert findAnagrams(test_s, test_p) == test_output
