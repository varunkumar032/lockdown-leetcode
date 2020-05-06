from solutions.day05_BuyAndSellStock import maxProfit

def test_day05_01():
    test_input = [7,1,5,3,6,4]
    test_output = 7
    assert maxProfit(test_input) == test_output

def test_day05_02():
    test_input = [1,2,3,4,5]
    test_output = 4
    assert maxProfit(test_input) == test_output

def test_day05_03():
    test_input = [7,6,4,3,1]
    test_output = 0
    assert maxProfit(test_input) == test_output

def test_day05_04():
    test_input = []
    test_output = 0
    assert maxProfit(test_input) == test_output

def test_day05_05():
    test_input = [1]
    test_output = 0
    assert maxProfit(test_input) == test_output
