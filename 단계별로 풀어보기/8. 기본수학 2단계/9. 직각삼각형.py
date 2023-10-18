while True:
    a, b, c = map(int, input().split())
    if a == 0 & b == 0 & c == 0:
        break
    else:
        if a*a + b*b == c*c or a*a == b*b + c*c or b*b == a*a +c*c:
            print("right")
        else:
            print("wrong")