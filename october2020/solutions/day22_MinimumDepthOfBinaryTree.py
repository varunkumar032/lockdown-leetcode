# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	if not root.right:
		return 1 + minDepth(root.left)
	if not root.left:
		return 1 + minDepth(root.right)
	return 1 + min(minDepth(root.left), minDepth(root.right))

# Alternate Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def minDepth(root):
#     def dfs(node):
#         if not node: return float("inf")
#         if not node.left and not node.right: return 1
#         return min(dfs(node.left), dfs(node.right)) + 1
#     res = dfs(root)
#     return res if res != float("inf") else 0
