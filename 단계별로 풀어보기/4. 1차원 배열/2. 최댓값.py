index = 9
lst = []
while index >= 1:
    a = int(input())
    lst.append(a)
    index -= 1
    if index == 0:
        print(max(lst))
        print(lst.index(max(lst)) + 1)