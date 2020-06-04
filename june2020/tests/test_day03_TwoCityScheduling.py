from solutions.day03_TwoCityScheduling import twoCitySchedCost

def test_day03_01():
    test_input = [[10,20],[30,200],[400,50],[30,20]]
    test_output = 110
    assert twoCitySchedCost(test_input) == test_output

def test_day03_02():
    test_input = [[10,20],[10,20],[10,20],[10,20]]
    test_output = 60
    assert twoCitySchedCost(test_input) == test_output

def test_day03_03():
    test_input = [[20,20],[100,200],[100,20],[20,20]]
    test_output = 160
    assert twoCitySchedCost(test_input) == test_output
