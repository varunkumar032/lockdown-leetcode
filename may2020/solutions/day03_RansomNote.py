# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

def canConstruct(ransomNote, magazine):
    ransomNoteSet = set(ransomNote)
    for item in ransomNoteSet:
        if ransomNote.count(item)>magazine.count(item):
            return False
    return True

# Alternate solution
# from collections import Counter
# def canConstruct(ransomNote, magazine):
#     ransomNoteCount = Counter(ransomNote)
#     magazineCount = Counter(magazine)
#     for key in ransomNoteCount:
#         if ransomNoteCount[key]>magazineCount[key]:
#             return False
#     return True
