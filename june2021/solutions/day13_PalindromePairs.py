# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
# so that the concatenation of the two words words[i] + words[j] is a palindrome.

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]

# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.

def palindromePairs(words):
	n = len(words)
	result = list()
	indexDict = dict()
	for i, item in enumerate(words):
		indexDict[item] = i

	# Case 1 - empty strings
	if "" in indexDict:
		for i in range(n):
			if i != indexDict[""] and isPalindrome(words[i]):
				result.append([i, indexDict[""]])
				result.append([indexDict[""], i])

	# Case 2 - reversed words
	for i in range(n):
		reversedWord = words[i][::-1]
		if reversedWord in indexDict and i != indexDict[reversedWord]:
			result.append([i, indexDict[reversedWord]])

	# Case 3 - split words and check each part
	for i in range(n):
		for k in range(1, len(words[i])):
			left = words[i][:k]
			right = words[i][k:]
			reversedRight = right[::-1]
			if isPalindrome(left) and reversedRight in indexDict:
				result.append([indexDict[reversedRight], i])
			reversedLeft = left[::-1]
			if isPalindrome(right) and reversedLeft in indexDict:
				result.append([i, indexDict[reversedLeft]])

	return result

def isPalindrome(string):
	return string == string[::-1]
