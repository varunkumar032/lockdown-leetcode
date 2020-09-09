from solutions.day08_SumOfRootToLeafBinaryNumbers import TreeNode, sumRootToLeaf

def test_day08_01():
    test_input_root = TreeNode(1)
    test_input_root.left = TreeNode(0)
    test_input_root.right = TreeNode(1)
    test_input_root.left.left = TreeNode(0)
    test_input_root.left.right = TreeNode(1)
    test_input_root.right.left = TreeNode(0)
    test_input_root.right.right = TreeNode(1)
    test_output = 22
    assert sumRootToLeaf(test_input_root) == test_output


def test_day08_02():
    test_input_root = TreeNode(1)
    test_input_root.left = TreeNode(0)
    test_input_root.right = TreeNode(1)
    test_output = 5
    assert sumRootToLeaf(test_input_root) == test_output

def test_day08_03():
    test_input_root = TreeNode(1)
    test_input_root.left = TreeNode(0)
    test_input_root.right = TreeNode(1)
    test_input_root.right.right = TreeNode(1)
    test_output = 9
    assert sumRootToLeaf(test_input_root) == test_output
