from solutions.day27_ConstructBinaryTreeFromInorderAndPostorderTraversal import TreeNode, buildTree

def getInorderOfTree(root):
    return getInorderOfTree(root.left) + [root.val] + getInorderOfTree(root.right) if root else []

def test_day24_01():
    test_inorder = [9,3,15,20,7]
    test_postorder = [9,15,7,20,3]
    test_output_root = TreeNode(3)
    test_output_root.left = TreeNode(9)
    test_output_root.right = TreeNode(20)
    test_output_root.right.left = TreeNode(15)
    test_output_root.right.right = TreeNode(7)
    assert getInorderOfTree(buildTree(test_inorder, test_postorder)) == getInorderOfTree(test_output_root)

def test_day24_02():
    test_inorder = [9,5,1,7,2,12,8,4,3,11]
    test_postorder = [9,1,2,12,7,5,3,11,4,8]
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
    assert getInorderOfTree(buildTree(test_inorder, test_postorder)) == getInorderOfTree(test_output_root)
