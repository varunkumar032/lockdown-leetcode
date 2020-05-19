from solutions.day18_PermutationInString import checkInclusion

def test_day18_01():
    test_s1 = "ab"
    test_s2 = "eidbaooo"
    test_output = True
    assert checkInclusion(test_s1, test_s2) == test_output

def test_day18_02():
    test_s1 = "eidbaooo"
    test_s2 = "ab"
    test_output = False
    assert checkInclusion(test_s1, test_s2) == test_output

def test_day18_03():
    test_s1 = "abc"
    test_s2 = "axbcayz"
    test_output = True
    assert checkInclusion(test_s1, test_s2) == test_output

def test_day18_04():
    test_s1 = "a"
    test_s2 = "bdcde"
    test_output = False
    assert checkInclusion(test_s1, test_s2) == test_output
