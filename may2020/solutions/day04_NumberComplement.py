# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Input: 5 -> 101
# Output: 2 -> 010

# Input: 1 -> 1
# Output: 0 -> 0

def bitwiseComplement(num):
    return int('1'*len(bin(num).replace('0b', '')), 2) ^ num

# Alternate Solution
# def bitwiseComplement(num):
#     temp = num
#     bit = 1
#     while temp:
#         num = num ^ bit
#         bit = bit << 1
#         temp = temp >> 1
#     return num
