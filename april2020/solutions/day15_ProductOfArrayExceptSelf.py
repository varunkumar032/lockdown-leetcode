# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Note: Please solve it without division and in O(n).

def productExceptSelf(nums):
    result  = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = nums[i-1] * result[i-1]
    R = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i] * R
        R = R * nums[i]
    return result
