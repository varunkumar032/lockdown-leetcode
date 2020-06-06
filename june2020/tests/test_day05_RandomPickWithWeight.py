from solutions.day05_RandomPickWithWeight import RandomPickWithWeight

def test_day05_01():
    test_weight = [1]
    test_obj = RandomPickWithWeight(test_weight)
    a = test_obj.pickIndex(0.5)
    b = test_obj.pickIndex(0.2)
    c = test_obj.pickIndex(0.9)
    assert (a, b, c) == (0, 0, 0)

def test_day05_02():
    test_weight = [1, 3]
    test_obj = RandomPickWithWeight(test_weight)
    a = test_obj.pickIndex(0.5)
    b = test_obj.pickIndex(1.5)
    c = test_obj.pickIndex(2.5)
    d = test_obj.pickIndex(3.5)
    e = test_obj.pickIndex(1)
    assert (a, b, c, d, e) == (0, 1, 1, 1, 0)

def test_day05_03():
    test_weight = [1, 3, 4]
    test_obj = RandomPickWithWeight(test_weight)
    a = test_obj.pickIndex(0.5)
    b = test_obj.pickIndex(2.5)
    c = test_obj.pickIndex(7.5)
    d = test_obj.pickIndex(8)
    e = test_obj.pickIndex(4)
    f = test_obj.pickIndex(1)
    assert (a, b, c, d, e, f) == (0, 1, 2, 2, 1, 0)
