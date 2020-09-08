from solutions.day07_WordPattern import wordPattern

def test_day07_01():
    test_pattern = "abba"
    test_str = "dog cat cat dog"
    test_output = True
    assert wordPattern(test_pattern, test_str) == test_output

def test_day07_02():
    test_pattern = "abba"
    test_str = "dog cat cat fish"
    test_output = False
    assert wordPattern(test_pattern, test_str) == test_output

def test_day07_03():
    test_pattern = "aaaa"
    test_str = "dog cat cat dog"
    test_output = False
    assert wordPattern(test_pattern, test_str) == test_output

def test_day07_04():
    test_pattern = "abba"
    test_str = "dog dog dog dog"
    test_output = False
    assert wordPattern(test_pattern, test_str) == test_output

def test_day07_05():
    test_pattern = "abbc"
    test_str = "dog cat cat dog"
    test_output = False
    assert wordPattern(test_pattern, test_str) == test_output

def test_day07_06():
    test_pattern = "aaa"
    test_str = "dog dog dog dog"
    test_output = False
    assert wordPattern(test_pattern, test_str) == test_output
