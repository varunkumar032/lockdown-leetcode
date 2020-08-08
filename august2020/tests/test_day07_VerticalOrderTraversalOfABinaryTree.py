from solutions.day07_VerticalOrderTraversalOfABinaryTree import TreeNode, verticalTraversal

def test_day07_01():
    test_root = TreeNode(3)
    test_root.left = TreeNode(9)
    test_root.right = TreeNode(20)
    test_root.right.left = TreeNode(15)
    test_root.right.right = TreeNode(7)
    test_output = [[9],[3,15],[20],[7]]
    assert verticalTraversal(test_root) == test_output

def test_day07_02():
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(7)
    test_output = [[4],[2],[1,5,6],[3],[7]]
    assert verticalTraversal(test_root) == test_output

def test_day07_03():
    test_root = TreeNode(6)
    test_root.right = TreeNode(5)
    test_root.right.left = TreeNode(4)
    test_root.right.left.right = TreeNode(3)
    test_root.right.left.right.left = TreeNode(2)
    test_root.right.left.right.left.right = TreeNode(1)
    test_output = [[6,4,2],[5,3,1]]
    assert verticalTraversal(test_root) == test_output
