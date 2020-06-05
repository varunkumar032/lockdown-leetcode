from solutions.day04_ReverseString import reverseString

def test_day04_01():
    test_input = ["h","e","l","l","o"]
    test_output = ["o","l","l","e","h"]
    reverseString(test_input)
    assert test_input == test_output

def test_day04_02():
    test_input = ["H","a","n","n","a","h"]
    test_output = ["h","a","n","n","a","H"]
    reverseString(test_input)
    assert test_input == test_output

def test_day04_03():
    test_input = ["H"]
    test_output = ["H"]
    reverseString(test_input)
    assert test_input == test_output
