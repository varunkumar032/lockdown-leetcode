from solutions.day06_QueueReconstructionByHeight import reconstructQueue

def test_day06_01():
    test_input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    test_output = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    assert reconstructQueue(test_input) == test_output

def test_day06_02():
    test_input = [[3,1], [4,2], [6,1], [8,0]]
    test_output = [[8,0], [3,1], [6,1], [4,2]]
    assert reconstructQueue(test_input) == test_output

def test_day06_03():
    test_input = [[5,2], [5,0], [5,1]]
    test_output = [[5,0], [5,1], [5,2]]
    assert reconstructQueue(test_input) == test_output
