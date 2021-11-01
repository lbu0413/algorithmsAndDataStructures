class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0

    def traverse(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
