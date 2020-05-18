# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter
def findAnagrams(s, p):
    startIndexResult = []
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p)])
    right = len(p)-1
    for i in range(len(s)-len(p)+1):
        if p_counter == s_counter:
            startIndexResult.append(i)
        right+=1
        if right<len(s):
            s_counter[s[right]] += 1
            if s_counter[s[i]] == 1:
                del s_counter[s[i]]
            else:
                s_counter[s[i]] -= 1
    return startIndexResult

# Alternate Solution:
# from collections import Counter
# def findAnagrams(s, p):
#     startIndexResult = []
#     for i in range(len(s)-len(p)+1):
#         if Counter(p) == Counter(s[i:i+len(p)]):
#             startIndexResult.append(i)
#     return startIndexResult

# Alternate Solution:
# def findAnagrams(s, p):
#     startIndexResult = []
#     for i in range(len(s)-len(p)+1):
#         if sorted(p) == sorted(s[i:i+len(p)]):
#             startIndexResult.append(i)
#     return startIndexResult
