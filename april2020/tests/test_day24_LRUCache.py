from solutions.day24_LRUCache import LRUCache

def test_day24_01():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    a = cache.get(1)
    cache.put(3, 3)
    b = cache.get(2)
    cache.put(4, 4)
    c = cache.get(1)
    d = cache.get(3)
    e = cache.get(4)
    assert (a, b, c, d, e) == (1, -1, -1, 3, 4)

def test_day24_02():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    a = cache.get(1)
    cache.put(3, 3)
    b = cache.get(3)
    c = cache.get(1)
    d = cache.get(3)
    cache.put(3, 1)
    e = cache.get(3)
    assert (a, b, c, d, e) == (-1, 3, -1, 3, 1)
