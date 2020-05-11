from solutions.day10_MinStack import MinStack

def test_day10_01():
    minStack = MinStack()
    a = minStack.push(-2)
    b = minStack.push(0)
    c = minStack.push(-3)
    d = minStack.getMin()
    e = minStack.pop()
    f = minStack.top()
    g = minStack.getMin()
    assert (a, b, c, d, e, f, g) == (None, None, None, -3, None, 0, -2)

def test_day10_02():
    minStack = MinStack()
    a = minStack.push(0)
    b = minStack.push(1)
    c = minStack.push(0)
    d = minStack.getMin()
    e = minStack.top()
    f = minStack.pop()
    g = minStack.getMin()
    h = minStack.top()
    assert (a, b, c, d, e, f, g, h) == (None, None, None, 0, 0, None, 0, 1)
