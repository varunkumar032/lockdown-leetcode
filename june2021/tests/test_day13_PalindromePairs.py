from solutions.day13_PalindromePairs import palindromePairs

def test_day13_01():
    test_words = ["abcd","dcba","lls","s","sssll"]
    test_output = [[0,1],[1,0],[3,2],[2,4]]
    test_result = palindromePairs(test_words)
    assert len(test_result) == len(test_output)
    for ans in test_output:
    	assert ans in test_result

def test_day13_02():
    test_words = ["bat","tab","cat"]
    test_output = [[0,1],[1,0]]
    test_result = palindromePairs(test_words)
    assert len(test_result) == len(test_output)
    for ans in test_output:
    	assert ans in test_result

def test_day13_03():
    test_words = ["a",""]
    test_output = [[0,1],[1,0]]
    test_result = palindromePairs(test_words)
    assert len(test_result) == len(test_output)
    for ans in test_output:
    	assert ans in test_result

def test_day13_04():
    test_words = ["a","abc","aba",""]
    test_output = [[0,3],[3,0],[2,3],[3,2]]
    test_result = palindromePairs(test_words)
    assert len(test_result) == len(test_output)
    for ans in test_output:
    	assert ans in test_result
