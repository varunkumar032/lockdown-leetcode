# Given an array of strings, group anagrams together.

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def groupAnagrams(strs):
    strDict = {}
    for string in strs:
        sortedStr = "".join(sorted(string))
        if sortedStr in strDict:
            strDict[sortedStr].append(string)
        else:
            strDict[sortedStr] = [string]
    return list(strDict.values())

# Alternate Solution:
# from collections import defaultdict
# def groupAnagrams(strs):
#     strDict = defaultdict(list)
#     for string in strs:
#         sortedStr = "".join(sorted(string))
#         strDict[sortedStr].append(string)
#     return list(strDict.values())
