# Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

def thirdMax(nums):
	firstMaxNum = secondMaxNum = thirdMaxNum = None
	for num in nums:
		if num == firstMaxNum or num == secondMaxNum or num == thirdMaxNum:
			continue
		if firstMaxNum is None or num > firstMaxNum:
			thirdMaxNum = secondMaxNum
			secondMaxNum = firstMaxNum
			firstMaxNum = num
		elif secondMaxNum is None or num > secondMaxNum:
			thirdMaxNum = secondMaxNum
			secondMaxNum = num
		elif thirdMaxNum is None or num > thirdMaxNum:
			thirdMaxNum = num
	return thirdMaxNum if thirdMaxNum is not None else firstMaxNum
