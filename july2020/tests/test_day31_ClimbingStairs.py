from solutions.day31_ClimbingStairs import climbStairs

def test_day31_01():
    test_input = 2
    test_output = 2
    assert climbStairs(test_input) == test_output

def test_day31_02():
    test_input = 3
    test_output = 3
    assert climbStairs(test_input) == test_output

def test_day31_03():
    test_input = 4
    test_output = 5
    assert climbStairs(test_input) == test_output
