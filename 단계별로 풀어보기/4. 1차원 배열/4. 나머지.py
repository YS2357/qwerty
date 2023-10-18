# N = list(input() for _ in range(10))
# lst = []
# for i in range(10):
#     lst.append(int(N[i])%42)
# a = 10
# for j in range(42):
#     if lst.count(j) > 1:
#         a -= (lst.count(j)-1)

# print(a)

lst = []
for _ in range(10):
    a = int(input())
    b = a%42
    lst.append(b)
s = set(lst)
print(len(s))