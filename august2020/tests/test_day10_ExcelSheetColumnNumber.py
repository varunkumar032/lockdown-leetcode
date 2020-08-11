from solutions.day10_ExcelSheetColumnNumber import titleToNumber

def test_day10_01():
    test_input = "A"
    test_output = 1
    assert titleToNumber(test_input) == test_output

def test_day10_02():
    test_input = "AB"
    test_output = 28
    assert titleToNumber(test_input) == test_output

def test_day10_03():
    test_input = "ZY"
    test_output = 701
    assert titleToNumber(test_input) == test_output
