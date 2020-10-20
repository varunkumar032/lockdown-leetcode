from solutions.q05_SubarraysWithKDifferentIntegers import subarraysWithKDistinct

def test_q05_01():
    test_A = [1,2,1,2,3]
    test_K = 2
    test_output = 7
    assert subarraysWithKDistinct(test_A, test_K) == test_output

def test_q05_02():
    test_A = [1,2,1,2,4]
    test_K = 3
    test_output = 3
    assert subarraysWithKDistinct(test_A, test_K) == test_output

def test_q05_03():
    test_A = [1,2,1,2,1,2]
    test_K = 3
    test_output = 0
    assert subarraysWithKDistinct(test_A, test_K) == test_output

def test_q05_04():
    test_A = [1,2,1,2,1,2]
    test_K = 1
    test_output = 6
    assert subarraysWithKDistinct(test_A, test_K) == test_output
