x, y, w, h = map(int, input().split())

d1 = w - x
d2 = h - y
print(min(x, y, d1, d2))