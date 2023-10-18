n, x = map(int, input().split())
ser = list(map(int, input().split()))

for i in range(n):
    if ser[i] < x:
        print(ser[i], end = " ")


# n,x,*a=map(int,open(0).read().split())
# for i in a:i<x!=print(i)