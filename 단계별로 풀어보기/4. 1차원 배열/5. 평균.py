a = input()
b = list(map(int, input().split()))
c = []
M = max(b)
for i in b:
    c.append(i/M*100)
avg = sum(c)/len(b)
print(avg)