# Two images A and B are given, represented as binary, square matrices of the same size.  
# (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

# Example 1:
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.

def largestOverlap(A, B):
    maxOverlap = 0
    for row in range(-len(A)+1, len(A)):
        for col in range(-len(A)+1, len(A)):
            maxOverlap = max(maxOverlap, overlap(A, B, row, col))
    return maxOverlap

def overlap(A, B, rowOff, colOff):
    count = 0
    for row in range(len(A)):
        for col in range(len(A)):
            if (row+rowOff<0 or row+rowOff>=len(A)) or (col+colOff<0 or col+colOff>=len(A)):
                continue
            if (A[row][col] + B[row+rowOff][col+colOff] == 2):
                count += 1
    return count
