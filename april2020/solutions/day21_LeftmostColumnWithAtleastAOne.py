# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
# this row is sorted in non-decreasing order.
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
# If such index doesn't exist, return -1.

# Example 1:
# Input: mat = [[0,0],[1,1]]
# Output: 0

# Example 2:
# Input: mat = [[0,0],[0,1]]
# Output: 1

# Example 3:
# Input: mat = [[0,0],[0,0]]
# Output: -1

# Example 4:
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1

def leftMostColumnWithOne(mat):
    rows, cols = len(mat), len(mat[0])
    current_row = 0
    current_col = cols-1
    while current_row<rows and current_col>=0:
        if mat[current_row][current_col] == 0:
            current_row += 1
        else:
            current_col -= 1
    if current_col != cols-1:
        return current_col+1
    else:
        return -1
