from solutions.day03_ValidPalindrome import isPalindrome

def test_day03_01():
    test_input = "A man, a plan, a canal: Panama"
    test_output = True
    assert isPalindrome(test_input) == test_output

def test_day03_02():
    test_input = "race a car"
    test_output = False
    assert isPalindrome(test_input) == test_output

def test_day03_03():
    test_input = "Race car"
    test_output = True
    assert isPalindrome(test_input) == test_output

def test_day01_04():
    test_input = "0P"
    test_output = False
    assert isPalindrome(test_input) == test_output

def test_day03_05():
    test_input = "0P0"
    test_output = True
    assert isPalindrome(test_input) == test_output
