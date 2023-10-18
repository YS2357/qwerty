t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')        

# t = int(input())

# for i in range(t):
#     h, w, num = map(int, input().split())
#     if num%h == 0:
#         print(f'{h}0{num//h}')
#     else:
#         print(f'{num%h}0{(num//h) + 1}')
