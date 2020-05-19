# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
# the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(1, rows):
        grid[i][0] = grid[i][0] + grid[i-1][0]
    for j in range(1, cols):
        grid[0][j] = grid[0][j] + grid[0][j-1]
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

# Alternate Solution:
# def minPathSum(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     dp = [[0]*cols for _ in range(rows)]
#     for i in range(rows):
#         for j in range(cols):
#             dp[i][j] = grid[i][j]
#             if i>0 and j>0:
#                 dp[i][j] += min(dp[i-1][j], dp[i][j-1])
#             elif i>0:
#                 dp[i][j] += dp[i-1][j]
#             elif j>0:
#                 dp[i][j] += dp[i][j-1]
#     return dp[-1][-1]
