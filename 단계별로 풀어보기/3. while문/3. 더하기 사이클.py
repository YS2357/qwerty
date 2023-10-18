print("-"*32)
a = int(input())
b = a
index = 0
while 1:
    a = (a%10)*10 + ((a//10)+(a%10))%10
    print(a)
    index += 1
    if b == a:
        print("-"*32)
        print(index)
        break