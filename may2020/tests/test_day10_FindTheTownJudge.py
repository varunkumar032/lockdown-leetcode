from solutions.day10_FindTheTownJudge import findJudge

def test_day10_01():
    test_N = 2
    test_trust = [[1,2]]
    test_output = 2
    assert findJudge(test_N, test_trust) == test_output

def test_day10_02():
    test_N = 3
    test_trust = [[1,3],[2,3]]
    test_output = 3
    assert findJudge(test_N, test_trust) == test_output

def test_day10_03():
    test_N = 3
    test_trust = [[1,3],[2,3],[3,1]]
    test_output = -1
    assert findJudge(test_N, test_trust) == test_output

def test_day10_04():
    test_N = 3
    test_trust = [[1,2],[2,3]]
    test_output = -1
    assert findJudge(test_N, test_trust) == test_output

def test_day10_05():
    test_N = 4
    test_trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    test_output = 3
    assert findJudge(test_N, test_trust) == test_output

def test_day10_06():
    test_N = 1
    test_trust = []
    test_output = 1
    assert findJudge(test_N, test_trust) == test_output
