from solutions.day11_Subsets import subsets

def test_day11_01():
    test_input = [1,2,3]
    test_output = [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
    test_result = subsets(test_input)
    assert all([True if item in test_output else False for item in test_result]) and len(test_result)==len(test_output)

def test_day11_02():
    test_input = [1]
    test_output = [[], [1]]
    test_result = subsets(test_input)
    assert all([True if item in test_output else False for item in test_result]) and len(test_result)==len(test_output)