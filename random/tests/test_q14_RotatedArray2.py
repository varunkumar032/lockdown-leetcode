from solutions.q14_RotatedArray2 import rotatedArray2

def test_q14_01():
    test_nums = [4,5,6,7,1,2,3]
    test_queries = [2,6,8]
    test_output = [6,3,-1]
    assert rotatedArray2(test_nums, test_queries) == test_output

def test_q14_02():
    test_nums = [5,6,7,1,2,3,4]
    test_queries = [2,6,8]
    test_output = [5,2,-1]
    assert rotatedArray2(test_nums, test_queries) == test_output

def test_q14_03():
    test_nums = [1,2,3,4,5,6,7]
    test_queries = [2,6,8]
    test_output = [2,6,-1]
    assert rotatedArray2(test_nums, test_queries) == test_output
