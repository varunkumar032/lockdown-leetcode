# Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts 
# where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut 
# and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

# Example 1:
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

# Example 2:
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

# Example 3:
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9

def maxArea(h, w, horizontalCuts, verticalCuts):
	horizontalCuts.sort()
	verticalCuts.sort()
	if horizontalCuts[-1] < h:
		horizontalCuts.append(h)
	if verticalCuts[-1] < w:
		verticalCuts.append(w)
	maxHorizontalInterval = horizontalCuts[0]
	maxVerticalInterval = verticalCuts[0]
	for i in range(1, len(horizontalCuts)):
		maxHorizontalInterval = max(maxHorizontalInterval, horizontalCuts[i]-horizontalCuts[i-1])
	for i in range(1, len(verticalCuts)):
		maxVerticalInterval = max(maxVerticalInterval, verticalCuts[i]-verticalCuts[i-1])
	return (maxHorizontalInterval * maxVerticalInterval) % (10**9 + 7)
