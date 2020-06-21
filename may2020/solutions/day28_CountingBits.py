# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.

# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]

def countBits(num):
    resultArr = [0]
    for i in range(1, num+1):
        resultArr.append(resultArr[i//2] + i%2)
    return resultArr

# if num is even, number of 1s in num == number of 1s in num/2
# if num is odd, number of 1s in num == number of 1s in num/2 + 1

# Alternate Solution:
# def countBits(num):
#     resultArr = [0]
#     for i in range(1, num+1):
#         resultArr.append(resultArr[i>>1] + int(i&1))
#     return resultArr
