from solutions.day07_MinCostClimbingStairs import minCostClimbingStairs

def test_day07_01():
    test_cost = [10,15,20]
    test_output = 15
    assert minCostClimbingStairs(test_cost) == test_output

def test_day07_02():
    test_cost = [1,100,1,1,1,100,1,1,100,1]
    test_output = 6
    assert minCostClimbingStairs(test_cost) == test_output
