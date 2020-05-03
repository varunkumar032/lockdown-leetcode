from solutions.day02_JewelsAndStones import numJewelsInStones

def test_day02_01():
    J = "aA"
    S = "aAAbbbb"
    test_output = 3
    assert numJewelsInStones(J, S) == test_output

def test_day02_02():
    J = "z"
    S = "ZZ"
    test_output = 0
    assert numJewelsInStones(J, S) == test_output

def test_day02_03():
    J = "z"
    S = ""
    test_output = 0
    assert numJewelsInStones(J, S) == test_output

def test_day02_04():
    J = ""
    S = "ZZ"
    test_output = 0
    assert numJewelsInStones(J, S) == test_output
