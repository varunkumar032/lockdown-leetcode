from solutions.q07_SqrtX import mySqrt

def test_q07_01():
    test_x = 4
    test_output = 2
    assert mySqrt(test_x) == test_output

def test_q07_02():
    test_x = 8
    test_output = 2
    assert mySqrt(test_x) == test_output

def test_q07_03():
    test_x = 2147395599
    test_output = 46339
    assert mySqrt(test_x) == test_output
