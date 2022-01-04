n, m = map(int, input().split())


cards = [list(map(int, input().split())) for i in range(n)]

max_card = 0
for i in range(len(cards)):
    selected = min(cards[i])
    if selected > max_card:
        max_card = selected

print(max_card)
