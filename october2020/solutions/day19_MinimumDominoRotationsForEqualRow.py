# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino. 
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

# Example 1:
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

# Example 2:
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.

def minDominoRotations(A, B):
    minSwap = min(dominoRotations(A[0], A, B), 
                  dominoRotations(B[0], A, B), 
                  dominoRotations(A[0], B, A), 
                  dominoRotations(B[0], B, A))
    return -1 if minSwap==float('inf') else minSwap

def dominoRotations(target, r1, r2):
    numSwaps = 0
    for i in range(len(r1)):
        if r1[i]!=target and r2[i]!=target:
            return float('inf')
        elif r1[i]!=target:
            numSwaps += 1
    return numSwaps
