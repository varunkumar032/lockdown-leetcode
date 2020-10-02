from solutions.day01_NumberOfRecentCalls import RecentCounter

def test_day01_01():
    rc = RecentCounter()
    a = rc.ping(1)
    b = rc.ping(100)
    c = rc.ping(3001)
    d = rc.ping(3002)
    assert (a, b, c, d) == (1, 2, 3, 3)


def test_day01_02():
    rc = RecentCounter()
    a = rc.ping(1)
    b = rc.ping(3002)
    c = rc.ping(6003)
    d = rc.ping(9004)
    assert (a, b, c, d) == (1, 1, 1, 1)

def test_day01_03():
    rc = RecentCounter()
    a = rc.ping(1)
    b = rc.ping(3002)
    c = rc.ping(6003)
    d = rc.ping(9003)
    assert (a, b, c, d) == (1, 1, 1, 2)
