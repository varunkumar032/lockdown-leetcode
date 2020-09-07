from solutions.day04_PartitionLabels import partitionLabels

def test_day04_01():
    test_input = "ababcbacadefegdehijhklij"
    test_output = [9,7,8]
    assert partitionLabels(test_input) == test_output

def test_day04_02():
    test_input = "ababcbacadefegdehijhklia"
    test_output = [24]
    assert partitionLabels(test_input) == test_output

def test_day04_03():
    test_input = "abcdefghij"
    test_output = [1,1,1,1,1,1,1,1,1,1]
    assert partitionLabels(test_input) == test_output
