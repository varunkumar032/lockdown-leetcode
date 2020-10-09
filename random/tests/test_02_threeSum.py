from solutions.q02_threeSum import threeSum

def test_01():
    test_nums = [-1,0,1,2,-1,-4]
    test_answer = [[-1,-1,2],[-1,0,1]]
    test_output = threeSum(test_nums)
    assert len(test_answer) == len(test_output) and all([tuple(x) in test_output for x in map(sorted, test_answer)])

def test_02():
    test_nums = []
    test_answer = []
    test_output = threeSum(test_nums)
    assert len(test_answer) == len(test_output) and all([tuple(x) in test_output for x in map(sorted, test_answer)])

def test_03():
    test_nums = [0]
    test_answer = []
    test_output = threeSum(test_nums)
    assert len(test_answer) == len(test_output) and all([tuple(x) in test_output for x in map(sorted, test_answer)])

def test_04():
    test_nums = [0,0,0]
    test_answer = [[0,0,0]]
    test_output = threeSum(test_nums)
    assert len(test_answer) == len(test_output) and all([tuple(x) in test_output for x in map(sorted, test_answer)])

def test_05():
    test_nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    test_answer = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    test_output = threeSum(test_nums)
    assert len(test_answer) == len(test_output) and all([tuple(x) in test_output for x in map(sorted, test_answer)])
