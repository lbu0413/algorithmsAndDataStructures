import heapq as hq


a = []

while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, num)
