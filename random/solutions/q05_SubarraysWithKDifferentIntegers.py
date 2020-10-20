# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

# Return the number of good subarrays of A.

# Example 1:
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

# Example 2:
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

from collections import defaultdict

def subarraysWithKDistinct(A, K):
    if K == 1:
        return subarraysWithKAtmost(A, K)
    return subarraysWithKAtmost(A, K) - subarraysWithKAtmost(A, K-1)

def subarraysWithKAtmost(A, K):
    count = 0
    countDict = defaultdict(int)
    n = len(A)
    j = 0
    distinctCount = 0
    for i in range(n):
        while j < n and distinctCount <= K:
            if countDict[A[j]]==0:
                distinctCount += 1
            countDict[A[j]] += 1
            j += 1
        
        if distinctCount>K:
            count += j-i-1
        else:
            count += j-i
        
        countDict[A[i]] -= 1
        if countDict[A[i]]==0:
            distinctCount -= 1
    
    return count
