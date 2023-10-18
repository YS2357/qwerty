t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    for j in s:
        print(j*int(r), end="")
    print(end="\n")