import string

word = str(input().upper())
lst = []
for i in string.ascii_uppercase:
    lst.append(word.count(i))
# print(lst)
if lst.count(max(lst)) > 1:
    print("?")
else:
    index = lst.index(max(lst))
    # print(index)
    print(string.ascii_uppercase[index])