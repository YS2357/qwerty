a = int(input())
b = list(map(int, input().split()))
if len(b) > a:
    c = len(b) - a
    index = 0
    while 1:
        b.pop()
        index += 1
        if index == c:
            break
    print(min(b), max(b))


# a = int(input())
# b = list(map(int, input().split()))
# print(min(b), max(b))
