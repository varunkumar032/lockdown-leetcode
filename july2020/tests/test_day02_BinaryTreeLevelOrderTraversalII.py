from solutions.day02_BinaryTreeLevelOrderTraversalII import TreeNode, levelOrderBottom

def test_day02_01():
	test_root = TreeNode(3)
	test_root.left = TreeNode(9)
	test_root.right = TreeNode(20)
	test_root.right.left = TreeNode(15)
	test_root.right.right = TreeNode(7)
	test_output = [[15, 7], [9, 20], [3]]
	assert levelOrderBottom(test_root) == test_output

def test_day02_02():
	test_root = TreeNode(5)
	test_root.left = TreeNode(3)
	test_root.right = TreeNode(4)
	test_root.left.left = TreeNode(1)
	test_root.right.right = TreeNode(2)
	test_output = [[1, 2], [3, 4], [5]]
	assert levelOrderBottom(test_root) == test_output

def test_day02_03():
	test_root = TreeNode(5)
	test_root.right = TreeNode(4)
	test_root.right.right = TreeNode(3)
	test_root.right.right.right = TreeNode(2)
	test_root.right.right.right.right = TreeNode(1)
	test_output = [[1], [2], [3], [4], [5]]
	assert levelOrderBottom(test_root) == test_output
