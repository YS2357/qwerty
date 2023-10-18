num = str(input())
arr = []
for i in range(len(num)):
    arr.append(num[i])
arr.sort()
arr.reverse()
print(*arr, sep='')