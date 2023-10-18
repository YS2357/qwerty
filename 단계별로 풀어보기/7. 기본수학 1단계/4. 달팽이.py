import math 
a, b, v = map(int, input().split())
d = v - a
print(math.ceil(d/(a-b) + 1))