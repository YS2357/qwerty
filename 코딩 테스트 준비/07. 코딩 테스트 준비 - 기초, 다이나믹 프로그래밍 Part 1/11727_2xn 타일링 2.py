# 백준 11727번 문제 - 2×N 타일링 2
# 문제 설명:
# 2×N 크기의 직사각형을 1×2, 2×1, 2×2 타일로 채우는 방법의 수를 구하는 문제.
# N이 주어졌을 때, 가능한 타일 배치의 경우의 수를 동적 계획법을 통해 구함.

# 입력: 자연수 N (1 ≤ N ≤ 1000)
# 출력: 2×N 직사각형을 타일로 채우는 방법의 수를 10007로 나눈 나머지

# N을 입력받음
N = int(input())

# dp 테이블 생성 : dp[i]는 2xi 크기의 직사각형을 채우는 방법의 수를 저장
dp = [0] * (N + 1)

# 초기 조건 설정
dp[0] = 1
dp[1] = 1

# 2부터 N까지의 값들을 채움
for i in range(2, N + 1):
    # 점화식 : dp[i] = dp[i - 1] + 2 * dp[i -2]
    dp[i] = (dp[i - 1] + 2 * dp[i -2]) % 10007

# 결과 출력
print(dp[N])