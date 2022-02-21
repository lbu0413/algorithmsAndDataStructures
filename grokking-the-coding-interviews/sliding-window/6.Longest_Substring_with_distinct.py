# s = 'aabccbb'
s = 'abccde'

max_length = 0

window_sum, window_start = 0, 0
hsh = {}

for window_end in range(len(s)):
    right_char = s[window_end]
    # if the hash map already contains the 'right_char', shrink the window from the beginning
    # so that we have only one occurrence of 'right_char'
    if right_char in hsh:
        # this is tricky; in the current window, we will not have any 'right_char' after
        # its previous index and if 'window_start' is already ahead of the last index of
        # 'right_char', we will keep 'window_start'
        window_start = max(window_start, hsh[right_char] + 1)
        # insert the 'right_char' into the map
    hsh[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start+1)

print(max_length)
