# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Input: root = [1,2,3,4], x = 4, y = 3
#                 1
#               /   \
#              2      3
#             /
#            4
# Output: false

# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#                 1
#               /   \
#              2      3
#               \      \
#                4      5
# Output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x, y):
    if root is None:
        return False
    xinfo = []
    yinfo = []
    depth = 0
    parent = None
    dfs(root, x, y, depth, parent, xinfo, yinfo)
    return xinfo[0][0]==yinfo[0][0] and xinfo[0][1]!=yinfo[0][1]

def dfs(root, x, y, depth, parent, xinfo, yinfo):
    if root is None:
        return None
    if root.val == x:
        xinfo.append((depth, parent))
    if root.val == y:
        yinfo.append((depth, parent))
    dfs(root.left, x, y, depth+1, root, xinfo, yinfo)
    dfs(root.right, x, y, depth+1, root, xinfo, yinfo)
