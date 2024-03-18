#동형 그래프 찾기

import sys
from collections import defaultdict

n1, m1 = map(int, sys.stdin.readline().split())
graph1 = defaultdict(list) #defaultdict(list)는 존재하지 않는 키에 접근하면 빈 리스트 []를 값으로 생성
for _ in range(m1):
    x, y = map(int, sys.stdin.readline().split())
    graph1[x].append(y)
    graph1[y].append(x)

n2, m2 = map(int, sys.stdin.readline().split())
graph2 = defaultdict(list)
for _ in range(m2):
    x, y = map(int, sys.stdin.readline().split())
    graph2[x].append(y)
    graph2[y].append(x)
# print(graph1)

def diff(graph1,graph2):

    # 정점 수가 다르면 다른 그래프
    if n1 != n2:
        print("NO")
        return

    # 간선 수가 다르면 다른 그래프
    if (sum(len(node) for node in graph1.values()) // 2) != (sum(len(node) for node in graph2.values()) // 2):
        #모든 간선 수를 합하고, 반으로 나눠줘야 중복을 제거할 수 있다.
        print("NO")
        return

    # 정점 차수가 다르면 다른 그래프. 즉, 각 정점마다 가지는 선의 개수가 똑같아야 하므로 sort.
    degrees1 = sorted(len(node) for node in graph1.values())
    degrees2 = sorted(len(node) for node in graph2.values())
    if degrees1 != degrees2:
        print("NO")
        return
    #나머지 경우에는 YES
    print("YES")

diff(graph1,graph2)