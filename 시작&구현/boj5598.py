letters = input()

result = ""
for i in letters:
    original = ord(i) - 3
    if original < ord('A'):
        original += 26
    result += chr(original)

print(result)
