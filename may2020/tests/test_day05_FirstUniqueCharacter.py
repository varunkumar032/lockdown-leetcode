from solutions.day05_FirstUniqueCharacter import firstUniqChar

def test_day05_01():
    test_input = "leetcode"
    test_output = 0
    assert firstUniqChar(test_input) == test_output

def test_day05_02():
    test_input = "loveleetcode"
    test_output = 2
    assert firstUniqChar(test_input) == test_output

def test_day05_03():
    test_input = "aaaaa"
    test_output = -1
    assert firstUniqChar(test_input) == test_output

def test_day05_04():
    test_input = ""
    test_output =-1
    assert firstUniqChar(test_input) == test_output
