t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    d = y - x
    count = 0
    for j in range(1,999999999):
        d -= j
        count += 1
        if d > 0:
            d -= j
            count += 1
            if d <= 0:
                print(count)
                break
        elif d <= 0:
            print(count)
            break
    
""" 
1=1 = 1^2
11=2
121=4 = 2^2
1221=6
12321=9 = 3^2
123321=12
1234321=16 = 4^2
12344321=20
123454321=25 = 5^2
"""