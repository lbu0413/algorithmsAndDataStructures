
myList = []

for i in range(9):
    num = int(input())
    myList.append(num)

maximum = max(myList)
print('-----')
print(maximum)
print(myList.index(maximum)+1)
