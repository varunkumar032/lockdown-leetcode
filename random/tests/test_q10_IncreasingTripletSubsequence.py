from solutions.q10_IncreasingTripletSubsequence import increasingTriplet

def test_q10_01():
    test_nums = [1,2,3,4,5]
    test_output = True
    assert increasingTriplet(test_nums) == test_output

def test_q10_02():
    test_nums = [5,4,3,2,1]
    test_output = False
    assert increasingTriplet(test_nums) == test_output

def test_q10_03():
    test_nums = [2,1,5,0,4,6]
    test_output = True
    assert increasingTriplet(test_nums) == test_output

def test_q10_04():
    test_nums = [5,0,4,1,3,2]
    test_output = True
    assert increasingTriplet(test_nums) == test_output

def test_q10_05():
    test_nums = [1,2,2,2,2]
    test_output = False
    assert increasingTriplet(test_nums) == test_output
