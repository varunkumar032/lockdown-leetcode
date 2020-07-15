from solutions.day14_AngleBetweenHandsOfAClock import angleClock

def test_day14_01():
    test_hour = 12
    test_minutes =30
    test_output = 165
    assert angleClock(test_hour, test_minutes) == test_output

def test_day14_02():
    test_hour = 3
    test_minutes = 30
    test_output = 75
    assert angleClock(test_hour, test_minutes) == test_output

def test_day14_03():
    test_hour = 3
    test_minutes = 15
    test_output = 7.5
    assert angleClock(test_hour, test_minutes) == test_output

def test_day14_04():
    test_hour = 4
    test_minutes = 50
    test_output = 155
    assert angleClock(test_hour, test_minutes) == test_output

def test_day14_05():
    test_hour = 12
    test_minutes = 0
    test_output = 0
    assert angleClock(test_hour, test_minutes) == test_output
