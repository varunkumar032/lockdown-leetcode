# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

from collections import Counter
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_counter = Counter(s1)
    s2_counter = Counter(s2[:len(s1)])
    right = len(s1)-1
    for i in range(len(s2)-len(s1)+1):
        if s1_counter == s2_counter:
            return True
        right+=1
        if right<len(s2):
            s2_counter[s2[right]] += 1
            if s2_counter[s2[i]] == 1:
                del s2_counter[s2[i]]
            else:
                s2_counter[s2[i]] -= 1
    return False

# Alternate Solution:
# from collections import Counter
# def checkInclusion(s1, s2):
#     s1_counter = Counter(s1)
#     for i in range(len(s2)-len(s1)+1):
#         if s2[i] in s1 and s1_counter==Counter(s2[i:i+len(s1)]):
#             return True
#     return False
