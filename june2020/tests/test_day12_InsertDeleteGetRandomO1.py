from solutions.day12_InsertDeleteGetRandomO1 import RandomizedSet

def test_day12_01():
    randomSet = RandomizedSet()
    a = randomSet.insert(0)
    b = randomSet.insert(1)
    c = randomSet.remove(0)
    d = randomSet.insert(2)
    e = randomSet.remove(1)
    f = randomSet.getRandom()
    assert (a, b, c, d, e, f) == (True, True, True, True, True, 2)
