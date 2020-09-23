from solutions.day23_GasStation import canCompleteCircuit

def test_day23_01():
    test_gas = [1,2,3,4,5]
    test_cost = [3,4,5,1,2]
    test_output = 3
    assert canCompleteCircuit(test_gas, test_cost) == test_output

def test_day23_02():
    test_gas = [2,3,4]
    test_cost = [3,4,3]
    test_output = -1
    assert canCompleteCircuit(test_gas, test_cost) == test_output

def test_day23_03():
    test_gas = [5,1,2,3,4]
    test_cost = [4,4,1,5,1]
    test_output = 4
    assert canCompleteCircuit(test_gas, test_cost) == test_output
