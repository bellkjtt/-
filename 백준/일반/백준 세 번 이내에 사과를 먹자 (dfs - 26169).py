import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
graph=[]
visited=[[False] * 5 for _ in range(5)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
graph = [list(map(int, input().split())) for _ in range(5)]
r,c = map(int,input().split())

def dfs(x,y,depth, apple):
    visited[x][y]= True
    
    if graph[x][y] == 1:
        apple += 1

    if 2 <= apple:
        return 1

    if 2 < depth:
        visited[x][y] = False
        return 0

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < 5 and 0 <= xx < 5: #이거를 해주는 이유가 -1나 넘어가지 않게 하기 위해서
             if not visited[xx][yy] and graph[xx][yy] != -1: #0이나 1이고 아직 안갔다면
                if dfs(xx, yy, depth + 1, apple) == 1: #끝까지 돌렸을 때 1이면
                    return 1
    visited[x][y] = False #백트래킹이 없으면 반례 발생
    return 0

print(dfs(c, r, 0,0))