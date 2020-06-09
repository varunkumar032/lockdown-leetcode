# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false

def isPowerOfTwo(n):
    i = 1
    while i < n:
        i *= 2
    return i == n

# Alternate Solution:
# import math
# def isPowerOfTwo(n):
#     if n == 0:
#         return False
#     return math.floor(math.log2(n)) == math.ceil(math.log2(n))
