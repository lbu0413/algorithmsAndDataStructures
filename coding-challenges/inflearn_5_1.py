a, b = map(int, input().split())
a = list(map(int, str(a)))

stack = []
ans = ""
for i in a:
    while stack and b > 0 and stack[-1] < i:
        stack.pop()
        b -= 1
    stack.append(i)

if b > 0:
    stack = stack[:-b]
print(''.join(map(str, stack)))
