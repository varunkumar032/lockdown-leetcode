# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"

def longestPalindrome(s):
    def helper(l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    answer = ""
    for i in range(len(s)):
        substring = helper(i, i)
        if len(substring) > len(answer):
            answer = substring
        substring = helper(i, i+1)
        if len(substring) > len(answer):
            answer = substring
    return answer