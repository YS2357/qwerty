H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else :
    print(H-1, M+15) if H-1 >= 0 else print(23, M+15)


if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	