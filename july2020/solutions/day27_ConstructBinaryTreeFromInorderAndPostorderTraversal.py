# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
	if not inorder:
		return None

	right = postorder.pop()
	root = TreeNode(right)
	rootIndex = inorder.index(right)

	root.right = buildTree(inorder[rootIndex+1:], postorder)
	root.left = buildTree(inorder[:rootIndex], postorder)

	return root