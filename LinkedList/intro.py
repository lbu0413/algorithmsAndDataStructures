class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def printNodes(node=ListNode):
    current_node = node
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next


head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)

printNodes(head_node)


def printNodesRecursively(node=ListNode):
    print(node.val)
    if node.next is not None:
        printNodesRecursively(node.next)


printNodesRecursively(head_node)
