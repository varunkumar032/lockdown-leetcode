# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers.

# Example 1:
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    return getSum(root, 0)

def getSum(node, sum):
    if not node:
        return 0
    sum = (sum<<1) + node.val
    if not node.left and not node.right:
        return sum
    return getSum(node.left, sum) + getSum(node.right, sum)
