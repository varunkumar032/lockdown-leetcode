from solutions.day22_SortCharactersByFrequency import frequencySort

def test_day22_01():
    test_input = "tree"
    test_output_list = ["eert", "eetr"]
    assert frequencySort(test_input) in test_output_list

def test_day22_02():
    test_input = "cccaaa"
    test_output_list = ["cccaaa", "aaaccc"]
    assert frequencySort(test_input) in test_output_list

def test_day22_03():
    test_input = "Aabb"
    test_output_list = ["bbaA", "bbAa"]
    assert frequencySort(test_input) in test_output_list
