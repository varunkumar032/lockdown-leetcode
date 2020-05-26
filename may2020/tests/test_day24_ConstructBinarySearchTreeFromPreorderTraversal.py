from solutions.day24_ConstructBinarySearchTreeFromPreorderTraversal import TreeNode, bstFromPreorder

def getInorderOfBst(root):
    return getInorderOfBst(root.left) + [root.val] + getInorderOfBst(root.right) if root else []

def test_day24_01():
    test_input = [8,5,1,7,10,12]
    test_output_root = TreeNode(8)
    test_output_root.left = TreeNode(5)
    test_output_root.right = TreeNode(10)
    test_output_root.left.left = TreeNode(1)
    test_output_root.left.right = TreeNode(7)
    test_output_root.right.right = TreeNode(12)
    assert getInorderOfBst(bstFromPreorder(test_input)) == getInorderOfBst(test_output_root)

def test_day24_02():
    test_input = [3,2,1,4,5]
    test_output_root = TreeNode(3)
    test_output_root.left = TreeNode(2)
    test_output_root.right = TreeNode(4)
    test_output_root.left.left = TreeNode(1)
    test_output_root.right.right = TreeNode(5)
    assert getInorderOfBst(bstFromPreorder(test_input)) == getInorderOfBst(test_output_root)
