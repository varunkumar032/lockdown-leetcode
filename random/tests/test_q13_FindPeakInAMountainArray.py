from solutions.q13_FindPeakInAMountainArray import peakIndexInMountainArray

def test_q13_01():
    test_arr = [0,1,0]
    test_output = 1
    assert peakIndexInMountainArray(test_arr) == test_output

def test_q13_02():
    test_arr = [0,2,1,0]
    test_output = 1
    assert peakIndexInMountainArray(test_arr) == test_output

def test_q13_03():
    test_arr = [0,10,5,2]
    test_output = 1
    assert peakIndexInMountainArray(test_arr) == test_output

def test_q13_04():
    test_arr = [3,4,5,1]
    test_output = 2
    assert peakIndexInMountainArray(test_arr) == test_output

def test_q13_05():
    test_arr = [24,69,100,99,79,78,67,36,26,19]
    test_output = 2
    assert peakIndexInMountainArray(test_arr) == test_output
