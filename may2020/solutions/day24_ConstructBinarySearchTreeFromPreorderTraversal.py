# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
# and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node
# first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    head = TreeNode(preorder[0])
    for val in preorder[1:]:
        root = head
        while True:
            if val < root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            else:
                if root.right == None:
                    root.right = TreeNode(val)
                    break
                root = root.right
    return head
