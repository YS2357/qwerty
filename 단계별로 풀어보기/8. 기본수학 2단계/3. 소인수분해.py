num = int(input())

d = 2
while num != 1:
    if num % d == 0:
        num = num / d
        print(d)
    else:
        d += 1