n = int(input())
arr = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    arr.append((x_i, y_i))
arr.sort(key=lambda x : (x[1], x[0])) # lambda가 정렬목적의 함수인듯? x는 변수이름으로 설정인것같음
for i in range(n):
    print(arr[i][0], arr[i][1])