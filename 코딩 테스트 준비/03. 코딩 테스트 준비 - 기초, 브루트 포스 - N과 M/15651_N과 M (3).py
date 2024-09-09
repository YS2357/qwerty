# 백준 문제 15651: N과 M (3)

# 표준 입력을 사용하기 위한 sys 모듈 임포트
import sys
input = sys.stdin.read

# 입력을 한 번에 읽어오기
data = input().strip().split()

# 주어진 숫자 N과 M
N = int(data[0])
M = int(data[1])

# 결과를 저장할 리스트 초기화
result = []

# 백트래킹 함수 정의
def backtrack(depth):
    # 디버깅: 현재 함수 호출의 상태를 출력
    # print(f"backtrack(depth={depth}, result={result})")
    
    # M개의 숫자를 모두 선택한 경우 결과를 출력
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    # 1부터 N까지의 숫자에 대해 반복
    for i in range(1, N + 1):
        # 현재 숫자를 결과에 추가
        result.append(i)
        # 다음 깊이로 이동
        backtrack(depth + 1)
        # 백트래킹을 위해 숫자 제거
        result.pop()
        # 디버깅: 백트래킹 후 상태를 출력
        # print(f"backtrack after pop(depth={depth}, result={result})")

# 백트래킹 함수 호출 (깊이 0부터 시작)
backtrack(0)
