# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

def findMaxLength(nums):
    firstOccDict = {}
    firstOccDict[0] = -1
    maxLength = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in firstOccDict:
            maxLength = max(maxLength, i-firstOccDict[count])
        else:
            firstOccDict[count] = i
    return maxLength
