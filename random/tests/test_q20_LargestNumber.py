from solutions.q20_LargestNumber import largestNumber

def test_q20_01():
    test_nums = [10,2]
    test_output = "210"
    assert largestNumber(test_nums) == test_output

def test_q20_02():
    test_nums = [3,30,34,5,9]
    test_output = "9534330"
    assert largestNumber(test_nums) == test_output

def test_q20_03():
    test_nums = [1]
    test_output = "1"
    assert largestNumber(test_nums) == test_output

def test_q20_04():
    test_nums = [10]
    test_output = "10"
    assert largestNumber(test_nums) == test_output

def test_q20_05():
    test_nums = [0,0]
    test_output = "0"
    assert largestNumber(test_nums) == test_output
