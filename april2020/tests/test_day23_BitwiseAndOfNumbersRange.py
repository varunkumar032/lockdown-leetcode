from solutions.day23_BitwiseAndOfNumbersRange import rangeBitwiseAnd

def test_day23_01():
    test_input_m = 5
    test_input_n = 7
    test_output = 4
    assert rangeBitwiseAnd(test_input_m, test_input_n) == test_output

def test_day23_02():
    test_input_m = 0
    test_input_n = 1
    test_output = 0
    assert rangeBitwiseAnd(test_input_m, test_input_n) == test_output

def test_day23_03():
    test_input_m = 10
    test_input_n = 14
    test_output = 8
    assert rangeBitwiseAnd(test_input_m, test_input_n) == test_output
