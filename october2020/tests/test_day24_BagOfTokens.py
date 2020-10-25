from solutions.day24_BagOfTokens import bagOfTokensScore

def test_day24_01():
    test_tokens = [100]
    test_P = 50
    test_output = 0
    assert bagOfTokensScore(test_tokens, test_P) == test_output

def test_day24_02():
    test_tokens = [100,200]
    test_P = 150
    test_output = 1
    assert bagOfTokensScore(test_tokens, test_P) == test_output

def test_day24_03():
    test_tokens = [100,200,300,400]
    test_P = 200
    test_output = 2
    assert bagOfTokensScore(test_tokens, test_P) == test_output
