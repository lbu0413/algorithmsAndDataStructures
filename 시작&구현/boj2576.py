
container = []

for i in range(7):
    num = int(input())
    if num & 1:
        container.append(num)
if len(container) == 0:
    print(-1)
else:
    print(sum(container))
    print(min(container))
