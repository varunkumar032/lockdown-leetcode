# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

def twoCitySchedCost(costs):
    sortedCosts = sorted(costs, key=lambda x:x[0]-x[1])
    totalMinCost = 0
    for i in range(len(sortedCosts)):
        if i<len(sortedCosts)//2:
            totalMinCost += sortedCosts[i][0]
        else:
            totalMinCost += sortedCosts[i][1]
    return totalMinCost

# Alternate Solution:
# def twoCitySchedCost(costs):
#     sortedCosts = sorted(costs, key=lambda x:x[0]-x[1])
#     totalMinCost = 0
#     N = len(sortedCosts)//2
#     for i in range(N):
#         totalMinCost += sortedCosts[i][0] + sortedCosts[i+N][1]
#     return totalMinCost
