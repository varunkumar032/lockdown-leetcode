# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

# N = 2
# trust = [[1,2]]

# N = 3
# trust = [[1,3],[2,3]]

# N = 3
# trust = [[1,3],[2,3],[3,1]]

# N = 3
# trust = [[1,2],[2,3]]

# N = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

def findJudge(N, trust):
    countList = [0]*(N+1)
    for a, b in trust:
        countList[b] += 1
        countList[a] -= 1
    for i in range(1, N+1):
        if countList[i] == N-1:
            return i
    return -1

# Alternate Solution:
# from collections import defaultdict
# def findJudge(N, trust):
#     possibleJudges = list(range(1, N+1))
#     trustCount = defaultdict(int)
#     for a, b in trust:
#         trustCount[b]+=1
#         if a in possibleJudges:
#             possibleJudges.remove(a)
#     if possibleJudges and trustCount[possibleJudges[0]]==N-1:
#         return possibleJudges[0]
#     else:
#         return -1
