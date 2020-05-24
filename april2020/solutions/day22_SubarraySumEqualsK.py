# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

from collections import defaultdict
def subarraySum(nums, k):
    currentSum = 0
    count = 0
    sumCounts = defaultdict(int)
    sumCounts[0] = 1
    for num in nums:
        currentSum += num
        if currentSum-k in sumCounts:           # currentSum = k + sumAtAnIndex
            count += sumCounts[currentSum-k]
        sumCounts[currentSum] += 1
    return count
