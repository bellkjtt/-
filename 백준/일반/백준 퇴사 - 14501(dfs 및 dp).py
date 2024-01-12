import sys
input=sys.stdin.readline
N=int(input())

T=[0] *N
P=[0] *N

for i in range(N):
    T[i], P[i] = map(int,input().split())

dp = [0] * (N+1)
for i in range(N-1,-1,-1):
    if i+T[i]<=N:
        dp[i] = max(dp[i+T[i]]+P[i],dp[i+1])
    else:
        dp[i]=dp[i+1]
        continue

print(dp[0])

#dp 프로그래밍

import sys
input=sys.stdin.readline
N=int(input())

T=[0] *N
P=[0] *N

for i in range(N):
    T[i], P[i] = map(int,input().split())


def dfs(n,sum):
    global ans
    if n>=N:
        ans = max(ans,sum)
        return

    if n+T[n]<=N:
        dfs(n+T[n],sum+P[n])
    dfs(n+1,sum)

ans=0
dfs (0,0)
print(ans)

#백트래킹 dfs