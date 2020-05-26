# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

def intervalIntersection(A, B):
    a_ptr = 0
    b_ptr = 0
    intersecting_intervals = []
    while a_ptr<len(A) and b_ptr<len(B):
        start, end = max(A[a_ptr][0], B[b_ptr][0]), min(A[a_ptr][1], B[b_ptr][1])
        if start <= end:
            intersecting_intervals.append([start, end])
        if A[a_ptr][1] < B[b_ptr][1]:
            a_ptr += 1
        else:
            b_ptr += 1
    return intersecting_intervals
