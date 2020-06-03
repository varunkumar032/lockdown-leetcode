from solutions.day08_MiddleOfTheLinkedList import ListNode, middleNode

def listOfNodeVals(head):
    listOfNodeVals = []
    while head:
        listOfNodeVals.append(head.val)
        head = head.next
    return listOfNodeVals

def test_day08_01():
    test_input_node1 = ListNode(1)
    test_input_node2 = ListNode(2)
    test_input_node3 = ListNode(3)
    test_input_node4 = ListNode(4)
    test_input_node5 = ListNode(5)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_input_node4.next = test_input_node5
    test_output_node1 = ListNode(3)
    test_output_node2 = ListNode(4)
    test_output_node3 = ListNode(5)
    test_output_node1.next = test_output_node2
    test_output_node2.next = test_output_node3
    assert listOfNodeVals(middleNode(test_input_node1)) == listOfNodeVals(test_output_node1)

def test_day08_02():
    test_input_node1 = ListNode(1)
    test_input_node2 = ListNode(2)
    test_input_node3 = ListNode(3)
    test_input_node4 = ListNode(4)
    test_input_node5 = ListNode(5)
    test_input_node6 = ListNode(6)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_input_node4.next = test_input_node5
    test_input_node5.next = test_input_node6
    test_output_node1 = ListNode(4)
    test_output_node2 = ListNode(5)
    test_output_node3 = ListNode(6)
    test_output_node1.next = test_output_node2
    test_output_node2.next = test_output_node3
    assert listOfNodeVals(middleNode(test_input_node1)) == listOfNodeVals(test_output_node1)
