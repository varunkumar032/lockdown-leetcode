from solutions.day23_IntervalListIntersections import intervalIntersection

def test_day23_01():
    test_A = [[0,2],[5,10],[13,23],[24,25]]
    test_B = [[1,5],[8,12],[15,24],[25,26]]
    test_output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    assert intervalIntersection(test_A, test_B) == test_output

def test_day23_02():
    test_A = [[1,2], [5,6]]
    test_B = [[3,4], [7,8]]
    test_output = []
    assert intervalIntersection(test_A, test_B) == test_output

def test_day23_03():
    test_A = [[1,2], [3,4], [5,6]]
    test_B = [[2,3], [4,5], [6,7]]
    test_output = [[2,2], [3,3], [4,4], [5,5], [6,6]]
    assert intervalIntersection(test_A, test_B) == test_output
