import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
arr = list(sorted(set(lst)))

dic = {arr[i]:i for i in range(len(arr))}

for i in lst:
    print(dic[i],end=' ') # value를 넣으면 index가 나오는 dictionary의 성질 이용