# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
	output = [[]]
	for num in nums:
		output += [current + [num] for current in output]
	return output

# Alternate Solution:
# import copy

# def subsets(nums):
#     if len(nums) == 0:
#         return [[]]
#     temp = subsets(nums[1:])
#     result = copy.deepcopy(temp)
#     for i in range(len(temp)):
#         temp[i].append(nums[0])
#         result.append(temp[i])
#     return result
