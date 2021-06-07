from solutions.q12_ValidMountainArray import validMountainArray

def test_q12_01():
    test_arr = [2,1]
    test_output = False
    assert validMountainArray(test_arr) == test_output

def test_q12_02():
    test_arr = [3,5,5]
    test_output = False
    assert validMountainArray(test_arr) == test_output

def test_q12_03():
    test_arr = [0,3,2,1]
    test_output = True
    assert validMountainArray(test_arr) == test_output

def test_q12_04():
    test_arr = [0,2,3,4,5,2,1,0]
    test_output = True
    assert validMountainArray(test_arr) == test_output

def test_q12_05():
    test_arr = [0,2,3,3,5,2,1,0]
    test_output = False
    assert validMountainArray(test_arr) == test_output
