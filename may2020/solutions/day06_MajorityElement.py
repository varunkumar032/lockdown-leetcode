# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Input: [3,2,3]
# Output: 3

# Input: [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
    countDict = {}
    majorityElement = nums[0]
    for num in nums:
        if num not in countDict:
            countDict[num] = 1
        else:
            countDict[num] += 1
        if countDict[num] > countDict[majorityElement]:
            majorityElement = num
    return majorityElement

# Alternate Solution:
# def majorityElement(nums):
#     for i in set(nums):
#         if nums.count(i) > len(nums)/2:
#             return i

# Alternate Solution:
# def majorityElement(nums):
#     return sorted(nums)[len(nums)//2]

# Alternate Solution:
# from collections import Counter
# def majorityElement(nums):
#     counts = Counter(nums)
#     return max(counts.keys(), key=counts.get)
