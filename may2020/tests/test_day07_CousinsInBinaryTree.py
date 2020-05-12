from solutions.day07_CousinsInBinaryTree import TreeNode, isCousins

test_root = TreeNode(1)
test_root.left = TreeNode(2)
test_root.right = TreeNode(3)
test_root.left.left = TreeNode(4)
test_root.left.right = TreeNode(5)
test_root.right.left = TreeNode(6)

def test_day07_01():
    test_x = 2
    test_y = 3
    test_output = False
    assert isCousins(test_root, test_x, test_y) == test_output

def test_day07_02():
    test_x = 4
    test_y = 5
    test_output = False
    assert isCousins(test_root, test_x, test_y) == test_output

def test_day07_03():
    test_x = 4
    test_y = 6
    test_output = True
    assert isCousins(test_root, test_x, test_y) == test_output

def test_day07_04():
    test_x = 2
    test_y = 5
    test_output = False
    assert isCousins(test_root, test_x, test_y) == test_output

def test_day07_05():
    test_x = 2
    test_y = 6
    test_output = False
    assert isCousins(test_root, test_x, test_y) == test_output
