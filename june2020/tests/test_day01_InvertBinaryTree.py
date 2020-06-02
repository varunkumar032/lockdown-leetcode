from solutions.day01_InvertBinaryTree import TreeNode, invertTree

def getInorderOfBst(root):
    return getInorderOfBst(root.left) + [root.val] + getInorderOfBst(root.right) if root else []

def test_day01_01():
    test_root = TreeNode(4)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(7)
    test_root.left.left = TreeNode(1)
    test_root.left.right = TreeNode(3)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(9)
    test_output = [9,7,6,4,3,2,1]
    assert getInorderOfBst(invertTree(test_root)) == test_output

def test_day01_02():
    test_root = TreeNode(3)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(4)
    test_root.left.left = TreeNode(1)
    test_root.right.right = TreeNode(5)
    test_output = [5,4,3,2,1]
    assert getInorderOfBst(invertTree(test_root)) == test_output
