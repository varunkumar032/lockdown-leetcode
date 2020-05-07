from solutions.day06_GroupAnagrams import groupAnagrams

def test_day06_01():
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    test_output = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    assert groupAnagrams(test_input) == test_output

def test_day06_02():
    test_input = ["abc", "bac", "cba", "acb", "bca", "cab"]
    test_output = [["abc", "bac", "cba", "acb", "bca", "cab"]]
    assert groupAnagrams(test_input) == test_output
