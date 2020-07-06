from solutions.day05_HammingDistance import hammingDistance

def test_day05_01():
    test_x = 1
    test_y = 4
    test_output = 2
    assert hammingDistance(test_x, test_y) == test_output

def test_day05_02():
    test_x = 4
    test_y = 4
    test_output = 0
    assert hammingDistance(test_x, test_y) == test_output

def test_day05_03():
    test_x = 0
    test_y = 15
    test_output = 4
    assert hammingDistance(test_x, test_y) == test_output
