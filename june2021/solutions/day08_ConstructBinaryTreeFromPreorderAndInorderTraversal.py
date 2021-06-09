# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary 
# tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def buildTree(preorder, inorder):
	if len(inorder) == 0:
		return None
	root = TreeNode(preorder.pop(0))
	rootIndex = inorder.index(root.val)
	root.left = buildTree(preorder, inorder[:rootIndex])
	root.right = buildTree(preorder, inorder[rootIndex+1:])
	return root
