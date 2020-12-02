from solutions.day01_MaximumDepthOfBinaryTree import TreeNode, maxDepth

def test_day01_01():
    test_root = TreeNode(3)
    test_root.left = TreeNode(9)
    test_root.right = TreeNode(20)
    test_root.right.left = TreeNode(15)
    test_root.right.right = TreeNode(7)
    test_output = 3
    assert maxDepth(test_root) == test_output

def test_day01_02():
    test_root = TreeNode(1)
    test_root.right = TreeNode(2)
    test_output = 2
    assert maxDepth(test_root) == test_output

def test_day01_03():
    test_root = None
    test_output = 0
    assert maxDepth(test_root) == test_output

def test_day01_04():
    test_root = TreeNode(0)
    test_output = 1
    assert maxDepth(test_root) == test_output
