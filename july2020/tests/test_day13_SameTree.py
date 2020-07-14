from solutions.day13_SameTree import TreeNode, isSameTree

def test_day13_01():
    test_p_root = TreeNode(1)
    test_p_root.left = TreeNode(2)
    test_p_root.right = TreeNode(3)
    test_q_root = TreeNode(1)
    test_q_root.left = TreeNode(2)
    test_q_root.right = TreeNode(3)
    test_output = True
    assert isSameTree(test_p_root, test_q_root) == test_output

def test_day13_02():
    test_p_root = TreeNode(1)
    test_p_root.left = TreeNode(2)
    test_q_root = TreeNode(1)
    test_q_root.right = TreeNode(2)
    test_output = False
    assert isSameTree(test_p_root, test_q_root) == test_output

def test_day13_03():
    test_p_root = TreeNode(1)
    test_p_root.left = TreeNode(2)
    test_p_root.right = TreeNode(1)
    test_q_root = TreeNode(1)
    test_q_root.left = TreeNode(1)
    test_q_root.right = TreeNode(2)
    test_output = False
    assert isSameTree(test_p_root, test_q_root) == test_output
