from solutions.q17_SumOfMutatedArrayClosestToTarget import findBestValue

def test_q17_01():
    test_arr = [4,9,3]
    test_target = 10
    test_output = 3
    assert findBestValue(test_arr, test_target) == test_output

def test_q17_02():
    test_arr = [2,3,5]
    test_target = 10
    test_output = 5
    assert findBestValue(test_arr, test_target) == test_output

def test_q17_03():
    test_arr = [2,3,5]
    test_target = 11
    test_output = 5
    assert findBestValue(test_arr, test_target) == test_output

def test_q17_04():
    test_arr = [60864,25176,27249,21296,20204]
    test_target = 56803
    test_output = 11361
    assert findBestValue(test_arr, test_target) == test_output
