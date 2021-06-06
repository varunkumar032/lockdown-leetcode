# You are given an sorted array A of N integers. You are also given q queries, 
# each query consist of an integer X[i], you have to report first and last occurence of X[i] in A.
# If X[i] is not present in A, return -1 -1.

# Note :- A follows the zero based indexing.

# Constraints:
# 1 ≤ N, q ≤ 105
# 0 ≤ A[i], X[i] ≤ 109

# Example 1:
# Input:
# A = [1, 1, 3, 4, 4, 8, 8, 8]
# q = [2, 1, 8, 3]
# Output: [[-1, -1], [0, 1], [5, 7], [2, 2]]

def firstAndLast(A, q):
	answer = []
	for query in q:
		firstOcc = -1
		lastOcc = -1
		left = 0
		right = len(A)-1
		while left < right:
			mid = left + (right-left)//2
			if A[mid] >= query:
				right = mid
			else:
				left = mid + 1
		if A[left] == query:
			firstOcc = left
		if firstOcc != -1:
			left = 0
			right = len(A)-1
			while left < right:
				mid = left + (right-left+1)//2
				if A[mid] > query:
					right = mid - 1
				else:
					left = mid
			lastOcc = left
		answer.append([firstOcc, lastOcc])
	return answer
