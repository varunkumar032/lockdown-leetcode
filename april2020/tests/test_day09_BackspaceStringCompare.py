from solutions.day09_BackspaceStringCompare import backspaceCompare

def test_day09_01():
    test_S = "ab#c"
    test_T = "ad#c"
    test_output = True
    assert backspaceCompare(test_S, test_T) == test_output

def test_day09_02():
    test_S = "ab##"
    test_T = "c#d#"
    test_output = True
    assert backspaceCompare(test_S, test_T) == test_output

def test_day09_03():
    test_S = "a##c"
    test_T = "#a#c"
    test_output = True
    assert backspaceCompare(test_S, test_T) == test_output

def test_day09_04():
    test_S = "a#c"
    test_T = "b"
    test_output = False
    assert backspaceCompare(test_S, test_T) == test_output
