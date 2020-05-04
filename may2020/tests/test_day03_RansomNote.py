from solutions.day03_RansomNote import canConstruct

def test_day03_01():
    test_ransomNote = "a"
    test_magazine = "b"
    test_output = False
    assert canConstruct(test_ransomNote, test_magazine) == test_output

def test_day03_02():
    test_ransomNote = "aa"
    test_magazine = "ab"
    test_output = False
    assert canConstruct(test_ransomNote, test_magazine) == test_output

def test_day03_03():
    test_ransomNote = "aa"
    test_magazine = "aab"
    test_output = True
    assert canConstruct(test_ransomNote, test_magazine) == test_output

def test_day03_04():
    test_ransomNote = ""
    test_magazine = "abab"
    test_output = True
    assert canConstruct(test_ransomNote, test_magazine) == test_output

def test_day03_05():
    test_ransomNote = "abab"
    test_magazine = ""
    test_output = False
    assert canConstruct(test_ransomNote, test_magazine) == test_output
