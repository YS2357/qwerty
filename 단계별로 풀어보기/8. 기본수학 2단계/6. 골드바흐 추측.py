import math


limit = 10000
eratos = [True]*(limit + 1)
eratos[0] = False
eratos[1] = False

for i in range(2, int(math.sqrt(len(eratos))) + 1):
    if eratos[i] == True:
        for j in range(i + i, len(eratos), i):
            eratos[j] = False


t = int(input())

for _ in range(t):
    num = int(input())
    a = num//2
    b = a
    for _ in range(limit):
        if eratos[a] and eratos[b]:
            print(a, b)
            break
        a -= 1
        b += 1