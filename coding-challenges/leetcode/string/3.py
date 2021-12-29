def longestSubstring(s):
    left = 0
    substring = 0
    hsh = {}

    for right in range(len(s)):
        if s[right] not in hsh:
            substring = max(substring, right-left+1)

        else:
            if hsh[s[right]] < left:
                substring = max(substring, right-left+1)

            else:
                left = hsh[s[right]] + 1
        hsh[s[right]] = right
    return substring


s = "abcabcbb"
print(longestSubstring(s))
