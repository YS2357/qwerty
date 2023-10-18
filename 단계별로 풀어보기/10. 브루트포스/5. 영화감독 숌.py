# n = int(input())
# idx = 0

# for i in range(999999):
#     if "666" in str(i):
#         idx +=1
#         if idx == n:
#             print(i)
#             break
#         break
### 위의 풀이는 틀림 왜틀림??? ###

N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)