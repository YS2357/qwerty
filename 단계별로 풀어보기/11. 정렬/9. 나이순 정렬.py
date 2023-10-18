n = int(input())
arr = []
for i in range(n):
    x_i, y_i = map(str, input().split())
    arr.append((int(x_i), y_i))
arr.sort(key=lambda x : x[0])
for i in range(n):
    print(arr[i][0], arr[i][1])