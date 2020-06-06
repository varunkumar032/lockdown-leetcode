# Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.

# Example 1:
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]

# Example 2:
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument,
# the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

class RandomPickWithWeight:
    def __init__(self, w):
        self.prefixSum = []
        prefixSum = 0
        for weight in w:
            prefixSum += weight
            self.prefixSum.append(prefixSum)
        self.totalSum = prefixSum

    def pickIndex(self, randomNum):
        # randomNum = random.random() * self.totalSum
        low, high = 0, len(self.prefixSum)
        while low<=high:
            mid = (low+high)//2
            if randomNum > self.prefixSum[mid]:
                low = mid+1
            else:
                high = mid-1
        return low
