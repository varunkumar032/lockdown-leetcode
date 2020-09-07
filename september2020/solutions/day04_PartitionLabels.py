# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
# and return a list of integers representing the size of these parts.


# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

def partitionLabels(S):
    start, end = 0, 0
    result = []
    endIndex = {}
    for i in range(len(S)):
        endIndex[S[i]] = i
    for i in range(len(S)):
        end = max(end, endIndex[S[i]])
        if i == end:
            result.append(end-start+1)
            start = i+1
    return result
