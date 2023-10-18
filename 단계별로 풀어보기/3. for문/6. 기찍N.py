n = int(input())
for i in range(n, 0, -1):  # n부터 1까지 역순
    print(i)

for i in range(1, n+1)[::-1]:
    print(i)

# [print(i) for i in range(1, int(input())+1)[::-1]]
