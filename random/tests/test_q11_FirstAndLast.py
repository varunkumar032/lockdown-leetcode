from solutions.q11_FirstAndLast import firstAndLast

def test_q11_01():
    test_A = [1, 1, 3, 4, 4, 8, 8, 8]
    test_q = [2, 1, 8, 3, 4]
    test_output = [[-1, -1], [0, 1], [5, 7], [2, 2], [3, 4]]
    assert firstAndLast(test_A, test_q) == test_output
