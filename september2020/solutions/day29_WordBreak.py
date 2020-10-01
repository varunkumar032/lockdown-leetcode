# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

def wordBreakHelper(s, wordSet):
	if not len(s):
		return True

	for i in range(1, len(s)+1):
		word = s[:i]
		if word in wordSet and wordBreakHelper(s[i:], wordSet):
			return True

	return False

def wordBreak(s, wordDict):
	return wordBreakHelper(s, set(wordDict))
