from solutions.q09_MaximumProductOfTwoElementsInAnArray import maxProduct

def test_q09_01():
    test_nums = [3,4,5,2]
    test_output = 12
    assert maxProduct(test_nums) == test_output

def test_q09_02():
    test_nums = [1,5,4,5]
    test_output = 16
    assert maxProduct(test_nums) == test_output

def test_q09_03():
    test_nums = [3,7]
    test_output = 12
    assert maxProduct(test_nums) == test_output
