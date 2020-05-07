# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Input: "leetcode"
# Output: 0

# Input: "loveleetcode"
# Output: 2

def firstUniqChar(s):
    countDict = {}
    for ch in s:
        if ch in countDict:
            countDict[ch] += 1
        else:
            countDict[ch] = 1
    for i, ch in enumerate(s):
        if countDict[ch] == 1:
            return i
    return -1

# Alternate Solution:
# from collections import Counter
# def firstUniqChar(s):
#     countDict = Counter(s)
#     for i, ch in enumerate(s):
#         if countDict[ch] == 1:
#             return i
#     return -1
