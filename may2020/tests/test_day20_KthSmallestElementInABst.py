from solutions.day20_KthSmallestElementInABst import TreeNode, kthSmallest

def test_day20_01():
    test_input_node1 = TreeNode(3)
    test_input_node2 = TreeNode(1)
    test_input_node3 = TreeNode(4)
    test_input_node4 = TreeNode(2)
    test_input_node1.left = test_input_node2
    test_input_node1.right = test_input_node3
    test_input_node2.right = test_input_node4
    test_input_k = 1
    test_output = 1
    assert kthSmallest(test_input_node1, test_input_k) == test_output

def test_day20_02():
    test_input_node1 = TreeNode(5)
    test_input_node2 = TreeNode(3)
    test_input_node3 = TreeNode(6)
    test_input_node4 = TreeNode(2)
    test_input_node5 = TreeNode(4)
    test_input_node6 = TreeNode(1)
    test_input_node1.left = test_input_node2
    test_input_node1.right = test_input_node3
    test_input_node2.left = test_input_node4
    test_input_node2.right = test_input_node5
    test_input_node4.left = test_input_node6
    test_input_k = 3
    test_output = 3
    assert kthSmallest(test_input_node1, test_input_k) == test_output
