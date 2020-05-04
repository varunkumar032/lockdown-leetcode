# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):
    sumAtIndex = maxSum = nums[0]
    for num in nums[1:]:
        sumAtIndex = max(sumAtIndex+num, num)
        maxSum = max(maxSum, sumAtIndex)
    return maxSum

# Alternate Solution:
# def maxSubArray(nums):
#     maxSumList = [nums[0]]
#     for num in nums[1:]:
#         if num > (maxSumList[-1]+num):
#             maxSumList.append(num)
#         else:
#             maxSumList.append(maxSumList[-1]+num)
#     return max(maxSumList)
