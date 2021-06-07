# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutive(nums):
	numSet = set(nums)
	maxLen = 0
	for num in numSet:
		if num-1 not in numSet:
			currLen = 1
			nextNum = num + 1
			while nextNum in numSet:
				currLen += 1
				nextNum += 1
			maxLen = max(maxLen, currLen)
	return maxLen
