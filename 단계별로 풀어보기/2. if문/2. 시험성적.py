score = int(input())
if score >= 90 :  # 조건1
    print('A')  # 조건1이 참인경우
elif score >= 80 :  # 조건2
    print('B')  # 조건2가 참인경우
elif score >= 70 :  # 조건3
    print('C')  # 조건3이 참인경우
elif score >= 60 :  # 조건4
    print('D')  # 조건4가 참인경우
else:
    print('F')  # 위 모든 조건이 거짓인 경우

print('A') if score >= 90 else print('B') if score >= 80 else print('C') if score >= 70 else print('D') if score >= 60 else print('F')
