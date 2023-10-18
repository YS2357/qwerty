x, y = map(str, input().split())
x = x[::-1]
y = y[::-1]
# print(x, y)
if int(x) > int(y):
    print(x)
else:
    print(y)