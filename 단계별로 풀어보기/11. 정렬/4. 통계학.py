import sys
from collections import Counter
n = int(input()) # 항상 홀수
arr = []
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()
nums_s = Counter(arr).most_common() # dict처럼 '이름:빈도수'로 저장
print(round(sum(arr)/n)) # 평균값
print(arr[int((n-1)/2)]) # 중앙값
# 두번째로 작은 최빈값
if len(nums_s) > 1: # 최빈값이 2개 이상인 경우
    if nums_s[0][1] == nums_s[1][1]: # 빈도수가 같은 경우
        print(nums_s[1][0]) # 두번째 값 출력
    else:
        print(nums_s[0][0]) # 아닌경우 
else: # [숫자][빈도수]
    print(nums_s[0][0])
print(arr[-1]-arr[0]) # 범위
# print(nums_s)