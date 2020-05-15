from solutions.day13_RemoveKDigits import removeKdigits

def test_day13_01():
    test_num = "1432219"
    test_k = 3
    test_output = "1219"
    assert removeKdigits(test_num, test_k) == test_output

def test_day13_02():
    test_num = "10"
    test_k = 2
    test_output = "0"
    assert removeKdigits(test_num, test_k) == test_output

def test_day13_03():
    test_num = "10"
    test_k = 1
    test_output = "0"
    assert removeKdigits(test_num, test_k) == test_output

def test_day13_04():
    test_num = "1234567890"
    test_k = 9
    test_output = "0"
    assert removeKdigits(test_num, test_k) == test_output

def test_day13_05():
    test_num = "123456789"
    test_k = 3
    test_output = "123456"
    assert removeKdigits(test_num, test_k) == test_output

def test_day13_06():
    test_num = "987654321"
    test_k = 3
    test_output = "654321"
    assert removeKdigits(test_num, test_k) == test_output

