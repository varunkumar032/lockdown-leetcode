# Invert a binary tree.

# Example:
# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root == None:
        return
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

# Alternate Solution:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def invertTree(root):
#     if root == None:
#         return
#     root.left, root.right = invertTree(root.right), invertTree(root.left)
#     return root
