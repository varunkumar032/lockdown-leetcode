# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.

def countSquares(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
    return sum([sum(row) for row in matrix])

# Alternate Solution:
# def countSquares(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     count = 0
#     for i in range(m):
#         for j in range(n):
#             if i>0 and j>0 and matrix[i][j] == 1:
#                 matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
#             count += matrix[i][j]
#     return count

# Alternate Solution:
# def countSquares(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     newMatrix = [[0]*(n+1) for _ in range(m+1)]
#     count = 0
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if matrix[i-1][j-1] == 1:
#                 newMatrix[i][j] = 1 + min(newMatrix[i-1][j], newMatrix[i-1][j-1], newMatrix[i][j-1])
#                 count += newMatrix[i][j]
#     return count
