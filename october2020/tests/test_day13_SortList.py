from solutions.day13_SortList import ListNode, sortList

def listOfNodeVals(head):
    listOfNodeVals = []
    while head:
        listOfNodeVals.append(head.val)
        head = head.next
    return listOfNodeVals

def test_day13_01():
    test_input_node1 = ListNode(4)
    test_input_node2 = ListNode(2)
    test_input_node3 = ListNode(1)
    test_input_node4 = ListNode(3)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_output_node1 = ListNode(1)
    test_output_node2 = ListNode(2)
    test_output_node3 = ListNode(3)
    test_output_node4 = ListNode(4)
    test_output_node1.next = test_output_node2
    test_output_node2.next = test_output_node3
    test_output_node3.next = test_output_node4
    assert listOfNodeVals(sortList(test_input_node1)) == listOfNodeVals(test_output_node1)

def test_day13_02():
    test_input_node1 = ListNode(-1)
    test_input_node2 = ListNode(5)
    test_input_node3 = ListNode(3)
    test_input_node4 = ListNode(4)
    test_input_node5 = ListNode(0)
    test_input_node1.next = test_input_node2
    test_input_node2.next = test_input_node3
    test_input_node3.next = test_input_node4
    test_input_node4.next = test_input_node5
    test_output_node1 = ListNode(-1)
    test_output_node2 = ListNode(0)
    test_output_node3 = ListNode(3)
    test_output_node4 = ListNode(4)
    test_output_node5 = ListNode(5)
    test_output_node1.next = test_output_node2
    test_output_node2.next = test_output_node3
    test_output_node3.next = test_output_node4
    test_output_node4.next = test_output_node5
    assert listOfNodeVals(sortList(test_input_node1)) == listOfNodeVals(test_output_node1)

def test_day13_03():
    test_input_node1 = None
    test_output_node1 = None
    assert listOfNodeVals(sortList(test_input_node1)) == listOfNodeVals(test_output_node1)
