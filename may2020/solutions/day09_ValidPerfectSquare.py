# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Input: 16
# Output: true

# Input: 14
# Output: false

def isPerfectSquare(num):
    low = 1
    high = num
    while low<=high:
        mid = (low+high)//2
        squareOfMid = mid*mid
        if squareOfMid == num:
            return True
        if squareOfMid>num:
            high = mid-1
        else:
            low = mid+1
    return False

# Alternate Solution:
# def isPerfectSquare(num):
#     i = 1
#     while num/i>=i:
#         if num == i*i:
#             return True
#         i+=1
#     return False
