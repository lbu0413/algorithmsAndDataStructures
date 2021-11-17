n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
calc = 0
for i in scores:
    calc += (i/max_score*100)

print(calc / len(scores))
