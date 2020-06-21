from solutions.day20_PermutationSequence import getPermutation

def test_day20_01():
    test_n = 3
    test_k = 3
    test_output = "213"
    assert getPermutation(test_n, test_k) == test_output

def test_day20_02():
    test_n = 4
    test_k = 9
    test_output = "2314"
    assert getPermutation(test_n, test_k) == test_output

def test_day20_03():
    test_n = 4
    test_k = 12
    test_output = "2431"
    assert getPermutation(test_n, test_k) == test_output

def test_day20_04():
    test_n = 4
    test_k = 13
    test_output = "3124"
    assert getPermutation(test_n, test_k) == test_output
