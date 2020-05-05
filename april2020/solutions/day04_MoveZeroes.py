# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note:
# 1. You must do this in-place without making a copy of the array.
# 2. Minimize the total number of operations.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    zeroIndex = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
            zeroIndex+=1

# Alternate Solution:
# def moveZeroes(nums):
#     nonZeroIndex = 0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[nonZeroIndex] = nums[i]
#             nonZeroIndex += 1
#     while nonZeroIndex<len(nums):
#         nums[nonZeroIndex] = 0
#         nonZeroIndex += 1

