# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

def maximalSquare(matrix):
    m, n = len(matrix), len(matrix[0])
    if not m:
        return 0
    maxHeight = 0
    dpMatrix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dpMatrix[i][j] = min(dpMatrix[i-1][j], dpMatrix[i-1][j-1], dpMatrix[i][j-1]) + 1
                maxHeight = max(maxHeight, dpMatrix[i][j])
    return maxHeight**2
