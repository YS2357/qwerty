# 백준 11052번 문제 - 카드 구매하기
# 문제 설명:
# 1부터 N장까지의 카드를 판매하는 카드팩이 있을 때,
# 카드 N장을 구매하기 위한 최대 금액을 구하는 문제.

# 입력: 자연수 N (1 ≤ N ≤ 1000), 카드팩 가격 리스트
# 출력: N장의 카드를 구매하는 데 필요한 최대 금액

# 입력 처리
N = int(input()) # 구매할 카드 수
prices = [0] + list(map(int, input().split())) # 카드팩 가격 리스트 (1-based index로 하기 위해 0 추가)

# dp 배열 생성 : dp[i]는 i개 카드를 구매할 때 얻을 수 있는 최대 금액을 저장
dp = [0] * (N + 1)

# 1부터 N까지 각 카드 수에 대해 최대 금액 계산
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + prices[j])

# 결과 출력 : N개의 카드를 구매할 때 최대 금액
print(dp[N])




# 디버깅 추가 버전


# # 백준 11052번 문제 - 카드 구매하기
# # 문제 설명:
# # 1부터 N장까지의 카드를 판매하는 카드팩이 있을 때,
# # 카드 N장을 구매하기 위한 최대 금액을 구하는 문제.

# # 입력: 자연수 N (1 ≤ N ≤ 1000), 카드팩 가격 리스트
# # 출력: N장의 카드를 구매하는 데 필요한 최대 금액

# # 입력 처리
# N = int(input())  # 구매할 카드 수
# prices = [0] + list(map(int, input().split()))  # 카드팩 가격 리스트 (1-based index로 하기 위해 0 추가)

# # dp 배열 생성: dp[i]는 i개의 카드를 구매할 때 얻을 수 있는 최대 금액을 저장
# dp = [0] * (N + 1)

# # 디버깅을 위한 출력 - 입력 확인
# print("입력받은 카드 개수 N:", N)
# print("카드팩 가격 리스트:", prices)

# # 1부터 N까지 각 카드 수에 대해 최대 금액 계산
# for i in range(1, N + 1):
#     print(f"\n현재 {i}개의 카드를 구매하려고 합니다.")
#     for j in range(1, i + 1):
#         # dp[i]의 현재 값과 새로 계산한 dp[i - j] + prices[j] 중 큰 값으로 갱신
#         print(f"  {j}개의 카드팩 선택 -> dp[{i}] = max(dp[{i}], dp[{i} - {j}] + prices[{j}]) = max({dp[i]}, {dp[i - j]} + {prices[j]})")
#         dp[i] = max(dp[i], dp[i - j] + prices[j])
#         print(f"  dp[{i}] 갱신 후 값: {dp[i]}")

# # 최종 결과 출력
# print("\n최종 dp 배열:", dp)
# print("N개의 카드를 구매할 때 최대 금액:", dp[N])