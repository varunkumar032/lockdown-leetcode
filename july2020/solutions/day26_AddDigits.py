# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

def addDigits(num):
    if len(str(num)) == 1:
        return num
    return addDigits(sum([int(x) for x in str(num)]))

# Alternate Solution:
# def addDigits(num):
#     if num%9 == 0 and num!=0:
#         return 9
#     else:
#         return num%9
