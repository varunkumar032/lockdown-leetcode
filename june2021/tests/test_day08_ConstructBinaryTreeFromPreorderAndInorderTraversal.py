from solutions.day08_ConstructBinaryTreeFromPreorderAndInorderTraversal import TreeNode, buildTree

def getInorderOfTree(root):
    return getInorderOfTree(root.left) + [root.val] + getInorderOfTree(root.right) if root else []

def test_day08_01():
    test_preorder = [3,9,20,15,7]
    test_inorder = [9,3,15,20,7]
    test_output_root = TreeNode(3)
    test_output_root.left = TreeNode(9)
    test_output_root.right = TreeNode(20)
    test_output_root.right.left = TreeNode(15)
    test_output_root.right.right = TreeNode(7)
    assert getInorderOfTree(buildTree(test_preorder, test_inorder)) == getInorderOfTree(test_output_root)

def test_day08_02():
    test_preorder = [-1]
    test_inorder = [-1]
    test_output_root = TreeNode(-1)
    assert getInorderOfTree(buildTree(test_preorder, test_inorder)) == getInorderOfTree(test_output_root)

def test_day08_03():
    test_preorder = [8,5,9,7,1,12,2,4,11,3]
    test_inorder = [9,5,1,7,2,12,8,4,3,11]
    test_output_root = TreeNode(8)
    test_output_root.left = TreeNode(5)
    test_output_root.left.left = TreeNode(9)
    test_output_root.left.right = TreeNode(7)
    test_output_root.left.right.left = TreeNode(1)
    test_output_root.left.right.right = TreeNode(12)
    test_output_root.left.right.right.left = TreeNode(2)
    test_output_root.right = TreeNode(4)
    test_output_root.right.right = TreeNode(11)
    test_output_root.right.right.left = TreeNode(3)
    assert getInorderOfTree(buildTree(test_preorder, test_inorder)) == getInorderOfTree(test_output_root)
