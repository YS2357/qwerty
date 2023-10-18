import sys
n = int(input())
arr = [0]*10001
for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] = arr[num] + 1 # 입력된 숫자에 해당하는 index에 +1
    # print(arr)
for i in range(10001):
    if arr[i] != 0: # 1, 2, 3, ...
        for j in range(arr[i]): # 중복되는 숫자가 얼마나 있는가?
            print(i) 