from solutions.day16_ValidParenthesisString import checkValidString

def test_day16_01():
    test_input = "()"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_02():
    test_input = "(*)"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_03():
    test_input = "(*))"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_04():
    test_input = "(*))("
    test_output = False
    assert checkValidString(test_input) == test_output

def test_day16_05():
    test_input = ")("
    test_output = False
    assert checkValidString(test_input) == test_output

def test_day16_06():
    test_input = "(**********)"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_07():
    test_input = "(**********"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_08():
    test_input = "**********"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_09():
    test_input = "(*()"
    test_output = True
    assert checkValidString(test_input) == test_output

def test_day16_10():
    test_input = "(*(*)))))"
    test_output = False
    assert checkValidString(test_input) == test_output
