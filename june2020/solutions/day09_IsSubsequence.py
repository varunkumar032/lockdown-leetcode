# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
# characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence.
# In this scenario, how would you change your code?

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(s, t):
    if len(s) == 0:
        return True
    for charInS in s:
        if len(t) == 0:
            return False
        i = 0
        while i<len(t):
            if t[i] == charInS:
                t = t[i+1:]
                break
            if i == len(t)-1:
                return False
            i += 1
    return True

# Alternate Solution
# def isSubsequence(s, t):
#     if len(s) == 0:
#         return True
#     if len(t) == 0:
#         return False
#     if s[0] == t[0]:
#         return isSubsequence(s[1:], t[1:])
#     return isSubsequence(s, t[1:])

# Alternate Solution
# def isSubsequence(s, t):
#     t = iter(t)                             # (x for x in t)
#     return all(char in t for char in s)
