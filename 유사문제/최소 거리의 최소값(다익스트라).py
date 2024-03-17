#1,1에서 n행 n열까지 도달하는 게 필요한 최소 값을 구하는 문제
#입력은 n행 n열에 각 칸마다 숫자가 주어진다.
#1행 1열에서 시작하므로 다익스트라로 풀었다

import heapq
INF = int(1e9) #무한을 의미하는 값으로 10억

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[float('inf')] * n for _ in range(n)] #거리 정보를 inf로 초기화
dist[0][0] = graph[0][0]


def dijkstra(n, graph):
    
    q = [(graph[0][0], 0, 0)] #그래프의 간선 정보 입력하기
    
    while q:
        cost, x, y = heapq.heappop(q) #힙에서 가장 최단 거리 노드 꺼내기
        if x == n-1 and y == n-1: #끝에 도달했다면
            return cost #cost 리턴
        if dist[x][y] < cost: #만약 이전에 발견한 cost가 더 작다면 skip
            continue
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #북남동서로
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n: #범위 안에 있다면
                new_cost = cost + graph[nx][ny] #new cost를 평가
                if new_cost < dist[nx][ny]: #만약에 현재 노드를 거쳤을 때의 새로운 코스트가 전의 코스트보다 작다
                    dist[nx][ny] = new_cost #갱신
                    heapq.heappush(q, (new_cost, nx, ny)) #힙에 넣는다.
    
    return -1

print(dijkstra(n, graph))