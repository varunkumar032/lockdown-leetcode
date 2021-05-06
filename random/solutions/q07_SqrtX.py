# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

def mySqrt(x):
    left, right = 0, x
    result = 0
    while left <= right:
        mid = left + (right-left)//2
        midsquare = mid * mid
        if midsquare == x:
            return mid
        elif midsquare < x:
            result = mid
            left = mid + 1
        else:
            right = mid -1
    return result
