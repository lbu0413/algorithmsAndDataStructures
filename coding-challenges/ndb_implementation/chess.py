position = input()
row = int(position[1])
col = int(ord(position[0]) - ord('a') + 1)

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]
cnt = 0

for step in steps:
    new_step = (row + step[0], col + step[1])
    if new_step[0] < 1 or new_step[1] < 1 or new_step[0] > 8 or new_step[1] > 8:
        continue
    cnt += 1

print(cnt)
