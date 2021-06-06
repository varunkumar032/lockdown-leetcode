from solutions.q08_ThirdMaximumNumber import thirdMax

def test_q08_01():
    test_nums = [3,2,1]
    test_output = 1
    assert thirdMax(test_nums) == test_output

def test_q08_02():
    test_nums = [1,2]
    test_output = 2
    assert thirdMax(test_nums) == test_output

def test_q08_03():
    test_nums = [2,2,3,1]
    test_output = 1
    assert thirdMax(test_nums) == test_output

def test_q08_04():
    test_nums = [3,3,4,3,4,3,0,3]
    test_output = 0
    assert thirdMax(test_nums) == test_output
