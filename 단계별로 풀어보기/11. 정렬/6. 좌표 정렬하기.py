n = int(input())
arr = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    arr.append((x_i, y_i))
arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])