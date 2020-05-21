# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    inorderList = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        inorderList.append(node.val)
        inorder(node.right)
    inorder(root)
    return inorderList[k-1]

# Alternate Solution:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def kthSmallest(root, k):
#     def inorder(root):
#         if root is None:
#             return []
#         in_left = inorder(root.left)
#         in_right = inorder(root.right)
#         return in_left + [root.val] + in_right
#     return inorder(root)[k-1]
