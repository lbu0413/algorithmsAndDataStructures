a = input()
stack = []
for i in a:
    if i.isalnum():
        stack.append(i)
    else:
        b = int(stack.pop())
        c = int(stack.pop())
        if i == '-':
            stack.append(c-b)
        if i == '+':
            stack.append(c+b)
        if i == '*':
            stack.append(c*b)
        if i == '/':
            stack.append(c/b)
print(stack.pop())
