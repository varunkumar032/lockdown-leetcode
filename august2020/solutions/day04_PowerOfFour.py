# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false

def isPowerOfFour(num):
    if num == 0:
        return False
    while num != 1:
        if num % 4:
            return False
        num = num // 4
    return True

# Alternate Solution:
# def isPowerOfFour(num):
# 	if num < 1:
# 		return False
# 	count = 0
# 	n = num
# 	while n > 1:
# 		n = n>>2
# 		count += 2
# 	return (n<<count) == num
