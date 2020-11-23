from solutions.day22_UniqueMorseCodeWords import uniqueMorseRepresentations

def test_day22_01():
    test_words = ["gin", "zen", "gig", "msg"]
    test_output = 2
    assert uniqueMorseRepresentations(test_words) == test_output

def test_day22_02():
    test_words = ["gin", "zen"]
    test_output = 1
    assert uniqueMorseRepresentations(test_words) == test_output

def test_day22_03():
    test_words = ["gin", "gig"]
    test_output = 2
    assert uniqueMorseRepresentations(test_words) == test_output
