a = int(input())
b = int(input())
c = int(input())
d = a*b*c
lst = list(map(int, str(d)))
# print(lst)
for i in range(0,10):
    print(lst.count(i))