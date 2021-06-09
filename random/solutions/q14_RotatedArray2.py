# Cheems gave an Array A of N distinct integers to rivalq. 
# rivalq being mischievous perform the following operation on the array.
# 	1. First sort the array in non-decreasing order.
# 	2. Then rotates the array between 1 and N times.

# Let the modified array be B. Cheems now wants to restore array A from the array B, therefore he will asks you q queries. 
# In each query you will be given some number num, you have to find its index (1-based) in B, if num is not present in B, print −1.

# Note:
# Rotating an array arr=[arr[1],arr[2],...arr[n]] 1 times results in arr=[arr[n],arr[1]...arr[n−1]]
# Example:

# N=5, q=3, B=[4,5,1,2,3]
# queries=[1,6,4]
# B is obtained from A=[1,2,3,4,5] by doing the rotation 2 times.
# 	1. Index of 1 in B is 3.
# 	2. 6 is not present in B, hence answer should be −1.
# 	3. Index of 4 in B is 1.

# Input:
# First line contains two integers: N and q.

# Second line contains N integers, where ith integer is B[i].

# Third line contains q integers, where ith integers is the number corresponds to ith query.

# Output:
# Print q lines, ith line should contains the answer to the ith query.

# Constraints:
# 1 ≤ N, q ≤ 10^5
# 0 ≤ B[i], num ≤ 10^9

def rotatedArray2(nums, queries):
	result = []
	n = len(nums)
	for query in queries:
		left = 0
		right = n - 1
		found = False
		while left <= right:
			mid = left + (right - left)//2
			if nums[mid] == query:
				result.append(mid+1)
				found = True
			if nums[mid] < nums[left]:
				if nums[mid] <= query <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1
			else:
				if nums[left] <= query <= nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
		if not found:
			result.append(-1)
	return result
