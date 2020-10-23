from solutions.day22_MinimumDepthOfBinaryTree import minDepth, TreeNode

def test_day22_01():
    test_root = TreeNode(3)
    test_root.left = TreeNode(9)
    test_root.right = TreeNode(20)
    test_root.right.left = TreeNode(15)
    test_root.right.right = TreeNode(7)
    test_output = 2
    assert minDepth(test_root) == test_output

def test_day22_02():
    test_root = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.right.right = TreeNode(4)
    test_root.right.right.right = TreeNode(5)
    test_root.right.right.right.right = TreeNode(6)
    test_output = 5
    assert minDepth(test_root) == test_output

def test_day22_03():
    test_root = TreeNode(3)
    test_root.left = TreeNode(2)
    test_root.left.right = TreeNode(1)
    test_root.right = TreeNode(4)
    test_root.right.right = TreeNode(5)
    test_output = 3
    assert minDepth(test_root) == test_output

def test_day22_04():
    test_root = TreeNode(1)
    test_output = 1
    assert minDepth(test_root) == test_output

def test_day22_05():
    test_root = None
    test_output = 0
    assert minDepth(test_root) == test_output
