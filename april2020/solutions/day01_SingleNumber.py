# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4

from functools import reduce
def singleNumber(nums):
    return reduce(lambda x, y:x^y, nums)

# Alternate Solution:
# def singleNumber(nums):
#     result = 0
#     for x in nums:
#         result ^= x
#     return result
