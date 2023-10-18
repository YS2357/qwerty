n = int(input())
result = 0
x = 0

for i in range(n):
    if i + sum(map(int, list(str(i)))) == n:
        result = max(result, i)
        break
print(result)