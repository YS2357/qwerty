a = int(input())
b = int(input())
lst = []

for num in range(a, b+1):
    count = 0
    if num > 1: # 다음 range(2,)이기에 1보다 큰수만
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            lst.append(num)
# print(lst)
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)