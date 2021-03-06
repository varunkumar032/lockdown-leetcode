# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5

def lengthOfLastWord(s):
    wordList = s.split()
    return len(wordList[-1]) if len(wordList) else 0

# Alternate Solution:
# def lengthOfLastWord(s):
#     return len(s.strip().split(" ")[-1])
