# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group.

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

def possibleBipartition(N, dislikes):
    if N<=1:
        return True
    while dislikes:
        g1 = set()
        g2 = set()
        g1.add(dislikes[0][0])
        g2.add(dislikes[0][1])
        rem = []
        for i in range(1, len(dislikes)):
            a, b = dislikes[i][0], dislikes[i][1]
            if a in g1 and b in g1:
                return False
            elif a in g2 and b in g2:
                return False
            elif a in g1 and b in g2:
                continue
            elif a in g2 and b in g1:
                continue
            elif a in g1:
                g2.add(b)
            elif b in g1:
                g2.add(a)
            elif a in g2:
                g1.add(b)
            elif b in g2:
                g1.add(a)
            else:
                rem.append(dislikes[i])
        dislikes = rem
    return True
