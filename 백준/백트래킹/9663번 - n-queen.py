n = int(input())

def is_safe(queens, col):
    row = len(queens)  # 현재 배치된 행의 개수 (다음 배치될 행)
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):  # 같은 열 또는 대각선 충돌 검사
            return False
    return True

def dfs(queens):
    if len(queens) == n:  # 모든 퀸을 배치한 경우
        return 1  # 가능한 경우의 수 하나 추가

    count = 0
    for col in range(n):  # 열 단위로 탐색
        if col in queens:
            continue
        if is_safe(queens, col):
            count += dfs(queens + [col])  # 가능한 경우의 수를 재귀적으로 더하기
    return count

print(dfs([]))


#pypy3로 했을때 정답 처리됨
#열의 조건과 대각선 조건만을 살피다.
#만약에 끝에 도달(col이 n과 같다면) 개수 1개를 추가한다
#같은 열이 아니고, 대각선에 배치되어 있지 않을때 True를 반환한다.
#그리고 True를 반환했을 떼, 비로소 해당 퀸에 해당 열을 append 형태로 추가해준다.
#만약에 이미 퀸이 배치되어 있다면 해당 열은 패스한다.(중요. 이 부분이 있어야 n=15에서 시간초과가 안남)