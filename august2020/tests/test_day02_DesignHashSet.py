from solutions.day02_DesignHashSet import MyHashSet

def test_day02_01():
    hashSet = MyHashSet()
    a = hashSet.add(1)
    b = hashSet.add(2)
    c = hashSet.contains(1)
    d = hashSet.contains(3)
    e = hashSet.add(2)
    f = hashSet.contains(2)
    g = hashSet.remove(2)
    h = hashSet.contains(2)
    assert (a, b, c, d, e, f, g, h) == (None, None, True, False, None, True, None, False)

def test_day02_02():
    hashSet = MyHashSet()
    a = hashSet.contains(1)
    b = hashSet.add(1)
    c = hashSet.contains(1)
    d = hashSet.remove(1)
    e = hashSet.contains(1)
    f = hashSet.add(2)
    g = hashSet.add(2)
    h = hashSet.contains(2)
    i = hashSet.remove(2)
    j = hashSet.contains(2)
    assert (a, b, c, d, e, f, g, h, i, j) == (False, None, True, None, False, None, None, True, None, False)
