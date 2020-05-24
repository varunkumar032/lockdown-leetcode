# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter
def frequencySort(s):
    sortedString = ""
    countDict = Counter(s)
    sortedCountList = sorted(countDict.items(), key=lambda x:x[1], reverse=True)
    return "".join(char*freq for char, freq in sortedCountList)

# Alternate Solution:
# def frequencySort(s):
#     sortedString = ""
#     countDict = {}
#     for char in s:
#         if char in countDict:
#             countDict[char] += 1
#         else:
#             countDict[char] = 1
#     sortedCharList = sorted(countDict, key=lambda x:countDict[x], reverse=True)
#     for char in sortedCharList:
#         sortedString += char * countDict[char]
#     return sortedString
