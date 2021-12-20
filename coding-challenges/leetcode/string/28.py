
def strStr(haystack, needle):
    h, n = len(haystack), len(needle)
    hash_needle = hash(needle)

    for i in range(h-n+1):
        if hash(haystack[i:i+n]) == hash_needle:
            return i

    return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))
