import sys

# 입력 크기
r, c = map(int, input().split())

# 보드 데이터
a = [list(i.rstrip()) for i in sys.stdin.readlines()]

# 방향 이동 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# while과 명시적인 스택을 이용한 백트래킹 구현
def dfs_with_while(start):
    stack = [(start, {a[start[0]][start[1]]})]  # (현재 좌표, 현재까지 방문한 알파벳 집합)
    max_len = 0  # 최대 경로 길이

    while stack:
        (x, y), alpha = stack.pop()  # 현재 상태
        max_len = max(max_len, len(alpha))  # 경로 길이 갱신

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:  # 경계 체크
                if a[nx][ny] not in alpha:  # 새로운 알파벳일 때
                    # 스택에 새로운 상태 추가
                    stack.append(((nx, ny), alpha | {a[nx][ny]}))

    return max_len

# DFS 시작
ans = dfs_with_while((0, 0))
print(ans)


#pypy3로 했을 때 7000ms로 아슬아슬하게 통과
#bfs로 하면 메모리 초과
#visited를 안 쓰면 더 좋다.

import sys

r, c = map(int,input().split())
# print(r,c)

a = [list(i.rstrip()) for i in sys.stdin.readlines()]

dx =[0,0,1,-1]
dy =[1,-1,0,0]

def dfs(x,y,alpha):
    max_len = 0
    alpha.add(a[x][y])
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<r and 0<=ny<c:
            if a[nx][ny] not in alpha:
                 max_len=max(max_len, dfs(nx,ny,alpha))
    alpha.remove(a[x][y])
    
    return max_len +1
alpha = set()
ans =dfs(0,0,alpha)
print(ans)

