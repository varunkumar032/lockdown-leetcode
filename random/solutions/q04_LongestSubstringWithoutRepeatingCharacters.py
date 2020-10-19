# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

from collections import defaultdict

def lengthOfLongestSubstring(s):
	n = len(s)
	maxLen = 0
	countDict = defaultdict(int)
	j = 0
	for i in range(n):
		# Skip re-initialization of j
		while j<n and countDict[s[j]]==0:
			countDict[s[j]] += 1
			j += 1

		# Taking the maximum
		maxLen = max(maxLen, j-i)
		if j==n:
			break

		# Updating the window
		countDict[s[i]] -= 1
	
	return maxLen
