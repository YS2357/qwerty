year = int(input())
A = year%4
# print(A)
B = year%100
# print(B)
C = year%400
# print(C)
if C == 0:
    print(1)
elif A == 0:
    if B == 0:
        print(0)
    else :
        print(1)
else : 
    print(0)



if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')