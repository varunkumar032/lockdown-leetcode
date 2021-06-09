from solutions.q15_FindTheSmallestDivisorGivenAThreshold import smallestDivisor

def test_q15_01():
    test_nums = [1,2,5,9]
    test_threshold = 6
    test_output = 5
    assert smallestDivisor(test_nums, test_threshold) == test_output

def test_q15_02():
    test_nums = [44,22,33,11,1]
    test_threshold = 5
    test_output = 44
    assert smallestDivisor(test_nums, test_threshold) == test_output

def test_q15_03():
    test_nums = [21212,10101,12121]
    test_threshold = 1000000
    test_output = 1
    assert smallestDivisor(test_nums, test_threshold) == test_output

def test_q15_04():
    test_nums = [2,3,5,7,11]
    test_threshold = 11
    test_output = 3
    assert smallestDivisor(test_nums, test_threshold) == test_output
