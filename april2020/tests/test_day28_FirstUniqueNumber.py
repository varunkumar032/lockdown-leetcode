from solutions.day28_FirstUniqueNumber import FirstUnique

def test_day28_01():
    firstUnique = FirstUnique([2,3,5])
    a = firstUnique.showFirstUnique()
    firstUnique.add(5)
    b = firstUnique.showFirstUnique()
    firstUnique.add(2)
    c = firstUnique.showFirstUnique()
    firstUnique.add(3)
    d = firstUnique.showFirstUnique()
    assert (a, b, c, d) == (2, 2, 3, -1)

def test_day28_02():
    firstUnique = FirstUnique([7,7,7,7,7,7])
    a = firstUnique.showFirstUnique()
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    b = firstUnique.showFirstUnique()
    assert (a, b) == (-1, 17)

def test_day28_03():
    firstUnique = FirstUnique([809])
    a = firstUnique.showFirstUnique()
    firstUnique.add(809)
    b = firstUnique.showFirstUnique()
    assert (a, b) == (809, -1)
