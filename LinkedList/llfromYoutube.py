class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            # 내 생각엔 맨 처음 self.head가 None으로 되있어서 그런거 같음.
            elems.append(cur.data)
        return elems

    def getIdx(self, idx):
        if idx < 0 or idx >= self.length():
            raise IndexError

        i = 0
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if i == idx:
                return cur.data
            i += 1

    def erase(self, idx):
        if idx < 0 or idx >= self.length():
            raise IndexError
        i = 0
        cur = self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
            if i == idx:
                prev.next = cur.next
                return
            i += 1


my_list = LinkedList()
my_list.append(2)
my_list.append(5)
my_list.append(28)
print(my_list.display())
print(my_list.getIdx(2))
my_list.erase(1)
print(my_list.display())
