# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

def minSubArrayLen(s, nums):
    n = len(nums)
    minLen = float('inf')
    currSum = 0
    j = 0
    for i in range(n):
        currSum += nums[i]
        while currSum >= s:
            minLen = min(minLen, i-j+1)
            currSum -= nums[j]
            j += 1
    return minLen if minLen != float('inf') else 0

# Alternate Solution:
# def minSubArrayLen(s, nums):
#     n = len(nums)
#     minLen = float('inf')
#     currSum = 0
#     j = 0
#     for i in range(n):
#         while currSum<s and j<n:
#             currSum += nums[j]
#             j += 1
#         if currSum < s:
#             break
#         minLen = min(minLen, j-i)
#         currSum -= nums[i]
#     return 0 if minLen == float('inf') else minLen
