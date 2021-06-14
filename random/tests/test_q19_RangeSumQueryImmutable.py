from solutions.q19_RangeSumQueryImmutable import NumArray

def test_q19_01():
    test_num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert test_num_array.sumRange(0, 2) == 1
    assert test_num_array.sumRange(2, 5) == -1
    assert test_num_array.sumRange(0, 5) == -3

def test_q19_02():
    test_num_array = NumArray([99])
    assert test_num_array.sumRange(0, 0) == 99
