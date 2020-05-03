# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Input: J = "aA", S = "aAAbbbb"
# Output: 3

def numJewelsInStones(J, S):
    count = 0
    for x in S:
        if x in J:
            count += 1
    return count

# Alternate solutions:
# def numJewelsInStones(J, S):
#     return sum(map(lambda x: x in J, S))

# def numJewelsInStones(J, S):
#     return len([x for x in S if x in J])
