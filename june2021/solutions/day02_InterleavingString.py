# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

def isInterleave(s1, s2, s3):
	if len(s1) + len(s2) != len(s3):
		return False

	memo = dict()
	def rec(i, j, k):
		if (i, j, k) in memo:
			return memo[(i, j, k)]
		if i==len(s1) and j==len(s2) and k==len(s3):
			return True
		result1, result2 = False, False
		if i<len(s1) and s1[i] == s3[k]:
			result1 = rec(i+1, j, k+1)
		if j<len(s2) and s2[j] == s3[k]:
			result2 = rec(i, j+1, k+1)
		memo[(i, j, k)] = result1 or result2
		return result1 or result2

	return rec(0, 0, 0)
