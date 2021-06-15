from solutions.day14_MaximumUnitsOnATruck import maximumUnits

def test_day14_01():
    test_boxTypes = [[1,3],[2,2],[3,1]]
    tets_truckSize = 4
    test_output = 8
    assert maximumUnits(test_boxTypes, tets_truckSize) == test_output

def test_day14_02():
    test_boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    tets_truckSize = 10
    test_output = 91
    assert maximumUnits(test_boxTypes, tets_truckSize) == test_output
