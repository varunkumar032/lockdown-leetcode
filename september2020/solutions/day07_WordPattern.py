# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

def wordPattern(pattern, string):
	patternDict = {}
	if len(string.split()) != len(pattern):
		return False
	for combo in zip(string.split(), pattern):
		if combo[0] in patternDict:
			if patternDict[combo[0]] != combo[1]:
				return False
		else:
			if combo[1] in patternDict.values():
				return False
			patternDict[combo[0]] = combo[1]		
	return True
