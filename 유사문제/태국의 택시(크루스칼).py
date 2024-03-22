import sys

def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)

    if u_root == v_root:
        return

    if rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    else:
        parent[u_root] = v_root
        if rank[u_root] == rank[v_root]:
            rank[v_root] += 1

def kruskal(nodes, n):
    nodes.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    total_cost = 0

    for node in nodes:
        u, v, cost = node
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += cost

    return total_cost

n, m = map(int, sys.stdin.readline().split())
nodes = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes.append((a - 1, b - 1, c))

min_cost = kruskal(nodes, n)
print(min_cost)


#n개의 마을과 m대의 택시가 있을 때, 택시만으로 모든 마을을 방문하는데 있어 드는 최소값
#크루스칼 알고리즘을 사용