from solutions.day02_DeleteNodeInALinkedList import ListNode, deleteNode

def listOfNodeVals(head):
    listOfNodeVals = []
    while head:
        listOfNodeVals.append(head.val)
        head = head.next
    return listOfNodeVals

def test_day02_01():
    test_input_node1 = ListNode(4)
    test_input_node2 = ListNode(5)
    test_input_node3 = ListNode(1)
    test_input_node4 = ListNode(9)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_head = test_input_node1
    test_toBeDeleted = test_input_node2
    test_output = [4,1,9]
    assert listOfNodeVals(deleteNode(test_head, test_toBeDeleted)) == test_output

def test_day02_02():
    test_input_node1 = ListNode(4)
    test_input_node2 = ListNode(5)
    test_input_node3 = ListNode(1)
    test_input_node4 = ListNode(9)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_head = test_input_node1
    test_toBeDeleted = test_input_node3
    test_output = [4,5,9]
    assert listOfNodeVals(deleteNode(test_head, test_toBeDeleted)) == test_output

def test_day02_03():
    test_input_node1 = ListNode(4)
    test_input_node2 = ListNode(5)
    test_input_node3 = ListNode(1)
    test_input_node4 = ListNode(9)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_head = test_input_node1
    test_toBeDeleted = test_input_node1
    test_output = [5,1,9]
    assert listOfNodeVals(deleteNode(test_head, test_toBeDeleted)) == test_output
