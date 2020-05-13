# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

def lastStoneWeight(stones):
    while len(stones)>1:
        stones.sort()
        x = stones.pop(-2)
        y = stones.pop(-1)
        if y-x:
            stones.append(y-x)
    if stones:
        return stones[0]
    else:
        return 0

# Alternate Solution:
# import heapq
# def lastStoneWeight(stones):
#     stones = [-i for i in stones]
#     heapq.heapify(stones)
#     while len(stones) > 1:
#         heavy1 = heapq.heappop(stones)
#         heavy2 = heapq.heappop(stones)
#         if heavy1 != heavy2:
#             heapq.heappush(stones, heavy1-heavy2)
#     return -heapq.heappop(stones) if stones else 0
