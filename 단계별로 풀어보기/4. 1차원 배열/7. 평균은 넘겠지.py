a = int(input())
for _ in range(a):
    lst = list(map(int, input().split()))
    s = 0
    for i in range(lst[0]):
        s += lst[i+1]
    avg = s/lst[0]
    cnt = 0
    for score in lst[1:]: # 인원수 제외하고 점수 세기
        if score > avg:
           cnt += 1
        elif score <= avg:
            cnt +=0
    print("%0.3f%%" % ((cnt/lst[0])*100)) 


# for i in[*open(0)][1:]:a,*b=map(int,i.split());print(f'{sum(a*j>sum(b)for j in b)/a:.3%}')