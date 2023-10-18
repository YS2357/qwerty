A, B = map(int, input().split())
if A > B:
    print('>')  # if 조건식이 참일 때 문장
elif A < B:
    print('<')  # if조건식이 참이 아닌경우 elif 조건식이 참일 때 문장
else:
    print('==')  # 위의 모든 조건이 거짓일 때 문장

### method 2
#### A,B = map(int,input().split())
print('>') if A > B else print('<') if A < B else print('==')