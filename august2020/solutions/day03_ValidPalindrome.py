# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

import re

def isPalindrome(s):
	alphaList = re.findall("[a-zA-Z0-9]+", s)	# alphaList = re.findall("[\w]+", s)
	alphaString = "".join(alphaList).lower()
	return alphaString == alphaString[::-1]

#Alternate Solution
# def isPalindrome(s):
# 	return (lambda x: x==x[::-1])([char for char in s.lower() if char.isalnum()])
