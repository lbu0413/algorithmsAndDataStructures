n = int(input())


for i in range(n):
    ps = input()
    stack = []
    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
