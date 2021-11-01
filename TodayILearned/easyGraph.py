import collections

starts = [1, 2, 3, 3]
ends = [2, 3, 1, 4]
N = 4
M = len(starts)

maps = collections.defaultdict(set)

for i in range(M):
    a = starts[i]
    b = ends[i]
    maps[a].add(b)
    maps[b].add(a)

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, len(maps[i]) + len(maps[j]) - (i in maps[j]))

print(ans)


# network rank of two cities is the total number of directly connected
# roads to either city
# A, B의 network rank는 A, B에 직접적으로 연결되어 있는 다른 도시의 개수의 총 합
# 만약 A와 B가 연결되어 있으면 하나만 카운트
