from solutions.q18_MagneticForceBetweenTwoBalls import maxDistance

def test_q18_01():
    test_position = [1,2,3,4,7]
    test_m = 3
    test_output = 3
    assert maxDistance(test_position, test_m) == test_output

def test_q18_02():
    test_position = [5,4,3,2,1,1000000000]
    test_m = 2
    test_output = 999999999
    assert maxDistance(test_position, test_m) == test_output

def test_q18_03():
    test_position = [1,5,8,11,13,16]
    test_m = 4
    test_output = 4
    assert maxDistance(test_position, test_m) == test_output
