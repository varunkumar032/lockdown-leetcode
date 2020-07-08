# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

# Example:
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i>0 and grid[i-1][j]==1:
                    perimeter -= 2
                if j>0 and grid[i][j-1]==1:
                    perimeter -= 2
    return perimeter

# Alternate Solution:
# def islandPerimeter(grid):
#     rows, cols = len(grid), len(grid[0])
#     def dfs(r, c):
#         if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
#             return 1
#         if grid[r][c] == 1:
#             grid[r][c] = 2
#             return dfs(r-1, c)+dfs(r+1, c)+dfs(r, c-1)+dfs(r, c+1)
#         return 0
#
#     perimeter = 0
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 1:
#                 perimeter += dfs(i, j)
#     return perimeter
