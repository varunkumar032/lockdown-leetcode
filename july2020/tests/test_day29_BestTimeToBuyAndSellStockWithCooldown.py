from solutions.day29_BestTimeToBuyAndSellStockWithCooldown import maxProfit

def test_day29_01():
    test_input = [1,2,3,0,2]
    test_output = 3
    assert maxProfit(test_input) == test_output

def test_day29_02():
    test_input = [1,2]
    test_output = 1
    assert maxProfit(test_input) == test_output

def test_day29_03():
    test_input = [1,0]
    test_output = 0
    assert maxProfit(test_input) == test_output

def test_day29_04():
    test_input = [1,5,1,1,1,1,5]
    test_output = 8
    assert maxProfit(test_input) == test_output
