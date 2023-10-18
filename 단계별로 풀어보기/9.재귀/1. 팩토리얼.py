n = int(input())
x = 1
if n == 0:
    print(1)
else:
    while n != 1:
        x *= n
        n -= 1
    print(x)


