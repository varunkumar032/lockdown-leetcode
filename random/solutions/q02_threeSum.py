# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

def threeSum(nums):
	nums.sort()
	n, result = len(nums), []
	for i in range(n-2):
		if i>0 and nums[i]==nums[i-1]:
			continue
		target = 0-nums[i]
		j, k = i+1, n-1
		while j<k:
			if nums[j]+nums[k]<target:
				j += 1
			elif nums[j]+nums[k]>target:
				k -= 1
			else:
				result.append((nums[i], nums[j], nums[k]))
				j += 1
				k -= 1
	return set(result)
