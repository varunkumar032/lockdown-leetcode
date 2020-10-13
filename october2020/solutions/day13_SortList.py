# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head
    mid = middleNode(head)
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def middleNode(head):
    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mid

def merge(l1, l2):
    dummyHead = ListNode(-1)
    currNode = dummyHead
    while l1 and l2:
        if l1.val<=l2.val:
            currNode.next = l1
            l1 = l1.next
        else:
            currNode.next = l2
            l2 = l2.next
        currNode = currNode.next
    if l1:
        currNode.next = l1
    else:
        currNode.next = l2
    return dummyHead.next
