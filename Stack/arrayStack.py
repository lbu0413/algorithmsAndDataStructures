# class ArrayStack:
#     def __init__(self):
#         self.data = []  # 빈 스택을 초기화

#     def size(self):
#         return len(self.data)  # 스택의 크기를 리턴

#     def isEmpty(self):
#         return self.size() == 0  # 스택이 비어 있는지 판단

#     def push(self, item):
#         self.data.append(item)

#     def pop(self):
#         return self.data.pop()

#     def peek(self):
#         return self.data[-1]


# class LinkedListStack:
#     def __init__(self):
#         self.data = DoublyLinkedList()

#     def size(self):
#         return self.data.getLength()

#     def isEmpty(self):
#         return self.size() == 0

#     def push(self, item):
#         node = Node(item)
#         self.data.insertAt(self.size() + 1, node)

#     def pop(self):
#         return self.data.popAt(self.size())

#     def peek(self):
#         return self.data.getAt(self.size()).data


# def solution(expr):
#     match = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#     S = ArrayStack()
#     for c in expr:
#         if c in '({[':
#             S.push(c)
#         elif c in match:
#             if S.isEmpty():
#                 return False
#             else:
#                 t = match[c]
#                 if t != S.pop():
#                     return False
#     return S.isEmpty()
#


a = '1ab2'
b = []
for i in range(len(a)):
    if a[i].isnumeric():
        b.append(a[i])

print(b)

# prec = {
#     '*': 3, '/': 3,
#     '+': 2, '-': 2,
#     '(': 1
# }
