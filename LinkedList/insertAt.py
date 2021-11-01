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

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        current = self.head
        while i < pos:
            current = current.next
            i += 1
        return current.data

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos-1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodecount + 1:
            self.tail = newNode
        return True


n1 = Node(1)
n2 = Node(40)
n3 = Node(24)
n4 = Node(3)
