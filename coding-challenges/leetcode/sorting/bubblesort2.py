def sort(num_strs):
    for idx in range(0, len(num_strs)-1):
        for i in range(0, len(num_strs)-idx-1):
            if num_strs[i][0] > num_strs[i+1][0]:
                num_strs[i], num_strs[i+1] = num_strs[i+1], num_strs[i]
    return num_strs


print(sort(num_strs=[(7, 'a'), (5, 'a'), (5, 'b'), (7, 'b'), (3, 'c')]))
