from solutions.day31_EditDistance import minDistance

def test_day31_01():
    test_word1 = "horse"
    test_word2 = "ros"
    test_output = 3
    assert minDistance(test_word1, test_word2) == test_output

def test_day31_02():
    test_word1 = "intention"
    test_word2 = "execution"
    test_output = 5
    assert minDistance(test_word1, test_word2) == test_output

def test_day31_03():
    test_word1 = "abc"
    test_word2 = "def"
    test_output = 3
    assert minDistance(test_word1, test_word2) == test_output

def test_day31_04():
    test_word1 = "abc"
    test_word2 = "abc"
    test_output = 0
    assert minDistance(test_word1, test_word2) == test_output
