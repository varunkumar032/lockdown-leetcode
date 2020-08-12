# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 3
# Output: [1,3,3,1]

def getRow(rowIndex):
	grid = [[1]*(i+1) for i in range(rowIndex+1)]
	for i in range(rowIndex+1):
		for j in range(i+1):
			if 0 < j < i:
				grid[i][j] = grid[i-1][j] + grid[i-1][j-1]
	return grid[rowIndex]
