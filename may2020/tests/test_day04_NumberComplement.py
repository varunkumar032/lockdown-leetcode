from solutions.day04_NumberComplement import bitwiseComplement

def test_day04_01():
    test_input = 5
    test_output = 2
    assert bitwiseComplement(test_input) == test_output

def test_day04_02():
    test_input = 1
    test_output = 0
    assert bitwiseComplement(test_input) == test_output

def test_day04_03():
    test_input = 7
    test_output = 0
    assert bitwiseComplement(test_input) == test_output

def test_day04_04():
    test_input = 10
    test_output = 5
    assert bitwiseComplement(test_input) == test_output
