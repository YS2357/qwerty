alpabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
index = len(word)
# print(len(word))

for i in alpabet:
    if i == "dz=":
        index -= word.count(i)
        # print(word.count(i))
        # print(index)
        # print("-----------")
    else:
        index -= word.count(i)
        # print(word.count(i))
        # print(index)
        # print("-----------")
print(index)


### method 2 ###

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))