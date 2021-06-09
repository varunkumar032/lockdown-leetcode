from solutions.q16_CapacityToShipPackagesWithinDDays import shipWithinDays

def test_q16_01():
    test_weights = [1,2,3,4,5,6,7,8,9,10]
    test_days = 5
    test_output = 15
    assert shipWithinDays(test_weights, test_days) == test_output

def test_q16_02():
    test_weights = [3,2,2,4,1,4]
    test_days = 3
    test_output = 6
    assert shipWithinDays(test_weights, test_days) == test_output

def test_q16_03():
    test_weights = [1,2,3,1,1]
    test_days = 4
    test_output = 3
    assert shipWithinDays(test_weights, test_days) == test_output
