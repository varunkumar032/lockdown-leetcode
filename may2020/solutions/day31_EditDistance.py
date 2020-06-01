# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

def minDistance(word1, word2):
    dpMatrix = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        for j in range(len(word2)+1):
            if i == 0:
                dpMatrix[i][j] = j
            elif j == 0:
                dpMatrix[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dpMatrix[i][j] = dpMatrix[i-1][j-1]
            else:
                dpMatrix[i][j] = min(dpMatrix[i][j-1], dpMatrix[i-1][j-1], dpMatrix[i-1][j]) + 1
    return dpMatrix[-1][-1]
