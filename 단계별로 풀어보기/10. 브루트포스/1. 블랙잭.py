# a,b = map(int, input().split())
# lst = list(map(int, input().split()))
# result = 0
# for i in range(a):
#     for j in range(i+1, a):
#         for k in range(j+1, a):
#             if lst[i] + lst[j] + lst[k] > b:
#                 continue
#             else:
#                 result = max(result, lst[i] + lst[j] + lst[k])
# print(result)

from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3)
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)