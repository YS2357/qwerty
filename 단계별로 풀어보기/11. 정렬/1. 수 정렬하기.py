n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
for _ in range(n):
    print(min(arr))
    arr.remove(min(arr))
# print(arr)

# x = int(input())
# num_list = []
# for i in range(x):
#     num_list.append(int(input()))
# num_list1 = sorted(num_list)
# for i in range(len(num_list)):
#     print(num_list1[i])