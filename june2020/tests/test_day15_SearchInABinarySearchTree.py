from solutions.day15_SearchInABinarySearchTree import TreeNode, searchBST

def test_day15_01():
    test_root = TreeNode(4)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(7)
    test_root.left.left = TreeNode(1)
    test_root.left.right = TreeNode(3)
    test_val = 2
    assert searchBST(test_root, test_val) == test_root.left

def test_day15_02():
    test_root = TreeNode(4)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(7)
    test_root.left.left = TreeNode(1)
    test_root.left.right = TreeNode(3)
    test_val = 5
    assert searchBST(test_root, test_val) == None
