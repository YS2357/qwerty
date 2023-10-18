### method 1
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

### method 2
# def solve(a):
#     return sum(a)


# lst = list(map(int, input().split()))
# a = 0
# # print(lst)
# while 1:
#     a += lst[0]
#     lst.reverse()
#     lst.pop()
#     if lst == []:
#         print(a)
#         break