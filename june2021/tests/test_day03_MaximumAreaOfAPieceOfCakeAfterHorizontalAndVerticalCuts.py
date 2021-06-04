from solutions.day03_MaximumAreaOfAPieceOfCakeAfterHorizontalAndVerticalCuts import maxArea

def test_day03_01():
    test_h = 5
    test_w = 4
    test_horizontalCuts = [1,2,4]
    test_verticalCuts = [1,3]
    test_output = 4
    assert maxArea(test_h, test_w, test_horizontalCuts, test_verticalCuts) == test_output

def test_day03_02():
    test_h = 5
    test_w = 4
    test_horizontalCuts = [3,1]
    test_verticalCuts = [1]
    test_output = 6
    assert maxArea(test_h, test_w, test_horizontalCuts, test_verticalCuts) == test_output

def test_day03_03():
    test_h = 5
    test_w = 4
    test_horizontalCuts = [3]
    test_verticalCuts = [3]
    test_output = 9
    assert maxArea(test_h, test_w, test_horizontalCuts, test_verticalCuts) == test_output
