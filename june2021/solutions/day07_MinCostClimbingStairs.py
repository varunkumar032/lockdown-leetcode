# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

def minCostClimbingStairs(cost):
	n = len(cost)
	if n == 0:
		return 0
	if n == 1:
		return cost[0]
	last = cost[1]
	secondLast = cost[0]
	for i in range(2, n):
		currCost = cost[i] + min(last, secondLast)
		secondLast = last
		last = currCost
	return min(last, secondLast)
