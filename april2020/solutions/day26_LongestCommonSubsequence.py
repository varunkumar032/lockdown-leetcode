# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec"
# is not). A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dpMatrix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if text1[j-1] == text2[i-1]:
                dpMatrix[i][j] = dpMatrix[i-1][j-1] + 1
            else:
                dpMatrix[i][j] = max(dpMatrix[i-1][j], dpMatrix[i][j-1])
    return dpMatrix[-1][-1]
