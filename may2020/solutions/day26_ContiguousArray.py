# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

def findMaxLength(nums):
    sumFirstIndexDict = {}
    sumFirstIndexDict[0] = -1
    maxLength = 0
    sumAtIndex = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            sumAtIndex -= 1
        else:
            sumAtIndex += 1
        if sumAtIndex in sumFirstIndexDict:
            maxLength = max(maxLength, i-sumFirstIndexDict[sumAtIndex])
        else:
            sumFirstIndexDict[sumAtIndex] = i
    return maxLength
