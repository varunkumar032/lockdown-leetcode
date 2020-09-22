from solutions.day21_CarPooling import carPooling

def test_day21_01():
    test_trips = [[2,1,5],[3,3,7]]
    test_capacity = 4
    test_output = False
    assert carPooling(test_trips, test_capacity) == test_output

def test_day21_02():
    test_trips = [[2,1,5],[3,3,7]]
    test_capacity = 5
    test_output = True
    assert carPooling(test_trips, test_capacity) == test_output

def test_day21_03():
    test_trips = [[2,1,5],[3,5,7]]
    test_capacity = 3
    test_output = True
    assert carPooling(test_trips, test_capacity) == test_output

def test_day21_04():
    test_trips = [[3,2,7],[3,7,9],[8,3,9]]
    test_capacity = 11
    test_output = True
    assert carPooling(test_trips, test_capacity) == test_output
