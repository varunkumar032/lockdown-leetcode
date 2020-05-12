# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there’re duplicates in arr, count them seperately.

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

def countElements(arr):
    return sum(1 for num in arr if num+1 in set(arr))

# Alternate Solution:
# def countElements(arr):
#     return sum(num+1 in set(arr) for num in arr)

# Alternate Solution:
# from collections import defaultdict
# def countElements(arr):
#     countDict = defaultdict(int)
#     for num in arr:
#         countDict[num]+=1
#     count = 0
#     for key in countDict:
#         if key+1 in countDict:
#             count+=countDict[key]
#     return count
