p = input()
stack = []

cnt = 0
for i in range(len(p)):
    if p[i] == '(':
        stack.append(p[i])
    else:
        if p[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            if stack:
                cnt += 1
                stack.pop()

print(cnt)
