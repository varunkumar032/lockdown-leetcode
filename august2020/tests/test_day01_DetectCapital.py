from solutions.day01_DetectCapital import detectCapitalUse

def test_day01_01():
    test_input = "USA"
    test_output = True
    assert detectCapitalUse(test_input) == test_output

def test_day01_02():
    test_input = "FlaG"
    test_output = False
    assert detectCapitalUse(test_input) == test_output

def test_day01_03():
    test_input = "Flag"
    test_output = True
    assert detectCapitalUse(test_input) == test_output

def test_day01_04():
    test_input = "flag"
    test_output = True
    assert detectCapitalUse(test_input) == test_output

def test_day01_05():
    test_input = "fLAG"
    test_output = False
    assert detectCapitalUse(test_input) == test_output
