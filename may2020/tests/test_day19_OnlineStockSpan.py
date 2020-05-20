from solutions.day19_OnlineStockSpan import StockSpanner

def test_day19_01():
    s = StockSpanner()
    a = s.next(100)
    b = s.next(80)
    c = s.next(60)
    d = s.next(70)
    e = s.next(60)
    f = s.next(75)
    g = s.next(85)
    assert (a, b, c, d, e, f, g) == (1, 1, 1, 2, 1, 4, 6)

def test_day19_02():
    s = StockSpanner()
    a = s.next(10)
    b = s.next(20)
    c = s.next(30)
    d = s.next(40)
    e = s.next(50)
    assert (a, b, c, d, e) == (1, 2, 3, 4, 5)

def test_day19_03():
    s = StockSpanner()
    a = s.next(50)
    b = s.next(40)
    c = s.next(30)
    d = s.next(20)
    e = s.next(10)
    assert (a, b, c, d, e) == (1, 1, 1, 1, 1)

def test_day19_04():
    s = StockSpanner()
    a = s.next(10)
    b = s.next(10)
    c = s.next(10)
    d = s.next(10)
    e = s.next(10)
    assert (a, b, c, d, e) == (1, 2, 3, 4, 5)
