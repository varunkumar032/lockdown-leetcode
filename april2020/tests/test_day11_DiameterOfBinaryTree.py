from solutions.day11_DiameterOfBinaryTree import TreeNode, diameterOfBinaryTree

def test_day11_01():
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_output = 3
    assert diameterOfBinaryTree(test_root) == test_output

def test_day11_02():
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.right.right = TreeNode(5)
    test_output = 4
    assert diameterOfBinaryTree(test_root) == test_output

def test_day11_03():
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_root.left.left.left = TreeNode(6)
    test_root.left.right.right = TreeNode(7)
    test_root.left.right.right.right = TreeNode(8)
    test_output = 5
    assert diameterOfBinaryTree(test_root) == test_output
