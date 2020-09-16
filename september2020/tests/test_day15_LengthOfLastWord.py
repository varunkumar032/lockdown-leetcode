from solutions.day15_LengthOfLastWord import lengthOfLastWord

def test_day15_01():
    test_input = "Hello World"
    test_output = 5
    assert lengthOfLastWord(test_input) == test_output

def test_day15_02():
    test_input = ""
    test_output = 0
    assert lengthOfLastWord(test_input) == test_output

def test_day15_03():
    test_input = " "
    test_output = 0
    assert lengthOfLastWord(test_input) == test_output
